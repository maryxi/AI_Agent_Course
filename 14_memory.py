import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.siliconflow.cn/v1")

print("启动终端聊天机器人 (输入 'quit' 退出)")

# 1. 【核心】在循环外部初始化记忆列表，设定简短的人设（PE）
messages = [
    {"role": "system", "content": "你是一个得力的编程助手。"}
]

# 2. 开启死循环，不断接收用户输入
while True:
    user_input = input("\n你: ")
    
    # 设定退出条件
    if user_input.lower() == "quit":
        print("聊天结束。")
        break

    # 3. 将用户的最新输入，追加(append)到记忆列表中
    messages.append({"role": "user", "content": user_input})

    # 4. 发送包含完整历史记录的 messages 给大模型
    try:
        response = client.chat.completions.create(
            model="Qwen/Qwen2.5-7B-Instruct",  # 换成阿里开源的免费模型，速度快不排队
            messages=messages,
            stream=False,
            stop=["user", "User:", "user:", "你:"] # 强行给模型戴上“嘴套”，禁止它自导自演
        )
        
        # 提取大模型的回复文本
        ai_reply = response.choices[0].message.content
        print(f"AI: {ai_reply}")
        
        # 5. 【极其重要】把 AI 的回复也追加到记忆列表中！
        # 如果不把 AI 的话存下来，上下文逻辑就会断裂
        messages.append({"role": "assistant", "content": ai_reply})
        
    except Exception as e:
        print(f"请求发生错误: {e}")

