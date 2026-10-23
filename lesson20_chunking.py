import os
import re

# ==========================================
# 第 20 课：Chunking 工程流水线实操演示
# 演示目标：将理论（解析、清洗、切分、重叠、元数据）落地为代码
# ==========================================

# 模拟我们从 PDF 中“解析(Parsing)”出来的原始文本。
# 实际工程中，你会使用 PyPDF2、pdfplumber 或更高级的 unstructured 库来提取。
# 假设这是我们提取出来的带有一定结构（标题、正文）和噪音（页眉、水印）的文本：
raw_pdf_text = """
--- 页眉：内部机密文档，严禁外传 ---
# 第一章：考勤与休假制度
这是第一章的正文内容。公司规定上班时间为 10:00。
迟到 10 分钟以内罚款 50 元。
(水印：公司内部专用)
## 1.1 年假规定
试用期员工不享受带薪年假。
转正后，第一年享有 5 天带薪年假。
--- 页脚：第 1 页 ---

--- 页眉：内部机密文档，严禁外传 ---
# 第二章：福利待遇
公司每天下午 15:00 提供下午茶。
每月最后周五为“带宠物上班日”。
(水印：公司内部专用)
## 2.1 报销规范
员工因公打车，每月报销额度不超过 1000 元。
餐饮报销仅限招待客户，标准不得超过 150 元/餐。
--- 页脚：第 2 页 ---
"""

def clean_text(text: str) -> str:
    """
    第一步：清洗 (Cleaning)
    理论：去除对大模型无用且干扰注意力的噪音，但绝不删除有用的结构信息。
    """
    print("\n--- 正在进行文本清洗 (Cleaning) ---")
    # 1. 洗掉页眉页脚 (使用正则表达式匹配特征)
    cleaned = re.sub(r'--- 页眉：.*? ---', '', text)
    cleaned = re.sub(r'--- 页脚：.*? ---', '', cleaned)
    
    # 2. 洗掉公司水印
    cleaned = re.sub(r'\(水印：.*?\)', '', cleaned)
    
    # 清除多余的空行
    cleaned = re.sub(r'\n+', '\n', cleaned).strip()
    
    print("✅ 清洗完成。去除了页眉、页脚和水印。")
    return cleaned

def chunk_by_structure(text: str, chunk_size: int, overlap: int) -> list:
    """
    第二步 & 第三步：策略切分 (Split Strategy) 与 重叠 (Overlap)
    理论：不要无脑按字数切！这里演示【按标题层级】结合【重叠】进行智能切分。
    """
    print(f"\n--- 正在进行结构化切块 (Chunk Size: {chunk_size}, Overlap: {overlap}) ---")
    
    # 1. 尝试按一级标题（#）进行粗切分，保留文档的大结构
    # 这样可以保证第一章和第二章的内容绝对不会混在一块卡片里
    sections = re.split(r'(?=# )', text)
    sections = [s.strip() for s in sections if s.strip()]
    
    chunks = []
    
    # 2. 对每个章节内部进行细切分，并加入 Overlap
    for section in sections:
        start = 0
        section_length = len(section)
        
        while start < section_length:
            end = start + chunk_size
            
            # 智能断句：尽量不要把一句话切成两半，寻找最近的换行符或句号
            if end < section_length:
                # 优先找换行符，其次找句号
                last_newline = section.rfind('\n', start, end)
                last_period = section.rfind('。', start, end)
                
                if last_newline != -1 and last_newline > start:
                    end = last_newline + 1
                elif last_period != -1 and last_period > start:
                    end = last_period + 1
            
            chunk_content = section[start:end].strip()
            if chunk_content:
                chunks.append(chunk_content)
                
            if end >= section_length:
                break
                
            # 加入重叠 (Overlap)：为了防止上下文断裂，往回退一段距离
            start = end - overlap

    return chunks

def add_metadata(chunks: list, source_name: str) -> list:
    """
    第四步：贴标签 (Metadata)
    理论：给知识卡片贴上来源、页码等标签，方便精准检索。
    """
    print("\n--- 正在附加元数据 (Metadata) ---")
    knowledge_cards = []
    for i, chunk in enumerate(chunks):
        card = {
            "content": chunk,
            "metadata": {
                "source": source_name,
                "chunk_id": f"chunk_{i}",
                # 实际工程中，这里还可以加上 page_number, author 等信息
            }
        }
        knowledge_cards.append(card)
    print(f"✅ 元数据附加完成。共生成 {len(knowledge_cards)} 张知识卡片。")
    return knowledge_cards


if __name__ == "__main__":
    print("=== 开始演示 Chunking 工程流水线 ===")
    
    # 演示：看看原始文本有多脏
    print("\n【原始文本 (带噪音)】:")
    print(raw_pdf_text[:150] + "...\n")
    
    # 1. 执行清洗
    clean_text_data = clean_text(raw_pdf_text)
    
    # 2. 执行切块 (演示 Overlap 的作用)
    # 设定每块比较小，故意制造切分，以观察 Overlap 效果
    chunks = chunk_by_structure(clean_text_data, chunk_size=50, overlap=20)
    
    # 3. 贴上元数据标签
    final_cards = add_metadata(chunks, source_name="公司员工手册.pdf")
    
    # 4. 打印最终结果，验证理论
    print("\n=== 最终的知识卡片 (Chunks) 展示 ===")
    for card in final_cards:
        print(f"🏷️ 标签 (Metadata): {card['metadata']}")
        print(f"📄 内容 (Content):\n{card['content']}")
        print("-" * 40)
