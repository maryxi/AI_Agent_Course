import os
from langchain_openai import ChatOpenAI, OpenAIEmbeddings, chat_openai


# ==========================================
# 演示重点：存入 ChromaDB 向量库，检索，并调用大模型生成答案
# ==========================================

SILICONFLOW_API_KEY = os.environ.get("DEEPSEEK_API_KEY")
CHAT_API_URL = "https://api.siliconflow.cn/v1/chat/completions"
CHAT_MODEL = "deepseek-ai/DeepSeek-V3"
llm = ChatOpenAI(model=CHAT_MODEL, api_key=SILICONFLOW_API_KEY, base_url=CHAT_API_URL)

# 初始化本地的 ChromaDB 客户端
# 数据会持久化存储在当前目录下的 'chroma_db' 文件夹中
chroma_client = chromadb.PersistentClient(path="./chroma_db")

# 创建或获取一个名为 "company_handbook" 的集合 (Collection)
# 集合就像是关系型数据库里的表
collection = chroma_client.get_or_create_collection(name="company_handbook")

def build_knowledge_base():
    """
    第一步：将文档切块，向量化，并存入 ChromaDB
    """
    print("=== 开始构建私有知识库 ===")
    
    # 如果库里已经有数据了，为了演示，我们先清空它 (实际生产中不需要)
    if collection.count() > 0:
        print("发现旧数据，正在清理...")
        collection.delete(where={}) # 简单起见，删除所有
    # 1. 切块
    cleaned_text = clean_text(raw_pdf_text)
    chunks = chunk_by_structure(cleaned_text, chunk_size=100, overlap=20)
    
    # 2. 存入数据库
    for i, chunk in enumerate(chunks):
        # 获取向量
        vector = get_embedding(chunk)
        if vector:
            # 存入 ChromaDB
            collection.add(
                embeddings=[vector],       # 文本的向量
                documents=[chunk],         # 原始文本卡片
                metadatas=[{"source": "奇葩员工手册", "chunk_id": i}], # 元数据
                ids=[f"chunk_{i}"]         # 唯一的 ID
            )
            print(f"✅ Chunk {i+1} 已存入向量库")
            
    print(f"知识库构建完成！共存入 {collection.count()} 条知识卡片。")

embedding = OpenAIEmbeddings(model="BAAI/bge-m3", api_key=SILICONFLOW_API_KEY, base_url=CHAT_API_URL)

def retrieve_and_generate(user_query: str):
    """
    第二步：用户提问 -> 检索 (Retrieval) -> 增强生成 (Generation)
    """
    print(f"\n🗣️ 用户提问: {user_query}")
    print("-" * 40)
    
    # --- R (Retrieval) 检索阶段 ---
    print("🔍 正在向量库中检索相关知识...")
    # 把用户的问题也变成向量
    query_vector = get_embedding(user_query)
    
    # 去库里搜索最相似的 top_k 个结果
    results = collection.query(
        query_embeddings=[query_vector],
        n_results=2 # 我们找最相关的 2 块
    )
    print("检索距离:", results['distances'][0])
    
    # 提取检索到的文本块
    retrieved_chunks = results['documents'][0]
    
    print("✅ 检索到的参考资料：")
    for i, text in enumerate(retrieved_chunks):
         print(f"  [{i+1}] {text}")
    print("-" * 40)
    
    # --- A (Augmented) & G (Generation) 增强生成阶段 ---
    print("🧠 正在请大模型基于参考资料生成答案...")
    
    # 把检索到的资料拼接到 Prompt 里，也就是“开卷考试”的参考书
    context = "\n".join(retrieved_chunks)
    
    system_prompt = f"""你是一个公司的资深 HR。请严格根据【参考资料】回答员工问题。

    【参考资料】：
    {context}

    回答要求：
    1. 优先使用参考资料中的信息作答。
    2. 如果参考资料中**没有明确提到**问题所问的内容，请如实回答"参考资料中未提及该信息"，不要自行推断或编造。
    3. 回答时尽量引用资料原文。"""

    headers = {
        "Authorization": f"Bearer {SILICONFLOW_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": CHAT_MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_query}
        ]
    }
    
    print("\n===== 发给大模型的完整 system_prompt =====")
    print(system_prompt)
    print("=" * 60)
    response = requests.post(CHAT_API_URL, headers=headers, json=payload)
    
    if response.status_code == 200:
        answer = response.json()["choices"][0]["message"]["content"]
        print("\n===== API 原始响应 =====")
        print(response.text)    
        print(f"\n🤖 大模型回答:\n{answer}")
    else:
        print(f"API 请求失败: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    if not SILICONFLOW_API_KEY:
         print("❌ 请先设置 DEEPSEEK_API_KEY 环境变量！")
         exit(1)
         
    # 1. 运行一次构建知识库
    build_knowledge_base()
    
    # 2. 模拟用户提问
    print("\n" + "="*50)
    # 测试问题 1：能检索到答案的
    retrieve_and_generate("试用期员工有年假吗？")
    
    print("\n" + "="*50)
    # 测试问题 2：手册里没有的，测试大模型会不会瞎编
    retrieve_and_generate("公司包晚餐吗？")
