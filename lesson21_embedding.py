import os
import requests
import json
import importlib
lesson20 = importlib.import_module("lesson20_chunking")
chunk_by_structure = lesson20.chunk_by_structure
clean_text = lesson20.clean_text
raw_pdf_text = lesson20.raw_pdf_text

# ==========================================
# 演示重点：调用硅基流 API，将文本转换为数字向量 (Embedding)
# ==========================================

# 硅基流 API 配置
SILICONFLOW_API_KEY = os.environ.get("DEEPSEEK_API_KEY") # 请确保环境变量中已配置此 KEY
# 注意：硅基流的 Embedding 接口地址和模型名称
EMBEDDING_API_URL = "https://api.siliconflow.cn/v1/embeddings"
# 硅基流支持的 embedding 模型，例如 BAAI/bge-m3 或 pro/BAAI/bge-m3
EMBEDDING_MODEL = "BAAI/bge-m3"
# EMBEDDING_MODEL = "Qwen/Qwen3-VL-Embedding-8B"
# "model": "" 

def get_embedding(text: str) -> list:
    """
    调用硅基流 API，获取一段文本的向量表示
    """
    if not SILICONFLOW_API_KEY:
         raise ValueError("请先设置 DEEPSEEK_API_KEY 环境变量！(这里使用的是硅基流的 API KEY)")

    headers = {
        "Authorization": f"Bearer {SILICONFLOW_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": EMBEDDING_MODEL,
        "input": text
    }
    
    print(f"正在将文本转换为向量... (模型: {EMBEDDING_MODEL})")
    # 忽略系统代理，避免本地代理未启动时请求失败
    session = requests.Session()
    session.trust_env = False
    response = session.post(EMBEDDING_API_URL, headers=headers, json=payload, timeout=60)
    
    if response.status_code == 200:
        data = response.json()
        # 提取向量数组
        vector = data["data"][0]["embedding"]
        return vector
    else:
        print(f"API 请求失败: {response.status_code}")
        print(response.text)
        return []

if __name__ == "__main__":
    print("=== 第 21 课：词向量计算 (Embedding) 演示 ===")
    
    # 1. 先复用第 20 课的代码，获取 Chunks
    cleaned_text = clean_text(raw_pdf_text)
    chunks = chunk_by_structure(cleaned_text, chunk_size=100, overlap=20)
    
    # 2. 拿第一个 Chunk 来演示向量化
    demo_chunk = chunks[0]
    print(f"\n我们要转换的文本内容是:\n{demo_chunk}\n")
    
    try:
        # 调用函数获取向量
        vector = get_embedding(demo_chunk)
        
        if vector:
            print(f"✅ 转换成功！")
            print(f"向量的维度是: {len(vector)} 维 (意思是计算机用 {len(vector)} 个数字来表示这段话)")
            print(f"向量的前 5 个数字长这样: {vector[:5]} ...")
    except Exception as e:
        print(f"出错了: {e}")
        print("提示: 演示前请在终端执行 `export DEEPSEEK_API_KEY=你的硅基流API_KEY`")
