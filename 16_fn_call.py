import json
import os
import requests

def get_weather(city):
    return f"{city}的天气是晴朗的, 温度是25摄氏度"

# ================= 1. 定义提供给大模型的工具列表 =================
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "获取城市的天气",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "城市名称"
                    }
                },
                "required": ["city"]
            }
        }
    }
]

api_key = os.environ.get('DEEPSEEK_API_KEY')
url = "https://api.siliconflow.cn/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# ================= 2. 第一次请求：询问大模型，让它决定是否调用工具 =================
messages = [
    {"role": "user", "content": "北京的天气今天怎么样？"}
]

payload = {
    "model": "deepseek-ai/DeepSeek-V3",
    "messages": messages,
    "tools": tools,
    "tool_call": "auto"
}

print("正在向大模型发送第一次数据请求...")
response = requests.post(url, headers=headers, json=payload)
msg = response.json()["choices"][0]["message"]

print("大模型的初步回复：")
print(json.dumps(msg, ensure_ascii=False, indent=2))

# ================= 3. 动态解析：判断模型是否想要调用工具 =================
if "tool_calls" in msg and msg["tool_calls"]:
    print("\n--- 检测到大模型想要调用本地函数！ ---")
    
    # 提取模型想调用的函数名和参数
    tool_call = msg["tool_calls"][0]
    function_name = tool_call["function"]["name"]
    arguments_dict = json.loads(tool_call["function"]["arguments"]) # 改名匹配你的模板
    
    print(f"大模型想调用的函数名是: {function_name}")
    print(f"大模型提取出的参数是: {arguments_dict}")
    
    # ================= 4. 动态路由与执行 =================
    available_functions = { 
        "get_weather": get_weather 
    } 
    
    if function_name in available_functions: 
        # 拿到对应的函数内存地址 
        func_to_call = available_functions[function_name] 
        
        print(f"\n[系统日志] 开始执行本地函数：{function_name} ...") 
        # 核心语法：使用 ** 解包字典，直接作为关键字参数传入 
        action_result = func_to_call(**arguments_dict) 
        
        print(f"[执行结果] 成功获取本地数据：{action_result}") 
        
        # ================= 5. 第二次请求：把结果喂给大模型 =================
        # 先把大模型那张“要求调用工具”的纸条存进历史记录
        messages.append(msg)
        # 再把我们执行的真实结果，伪装成 user 塞进去（为了兼容各种模型）
        messages.append({
            "role": "user",  
            "content": f"系统返回数据：{action_result}。请直接回答用户最初的问题。"
        })
        
        print("\n[系统日志] 正在发起第二次网络请求，等待模型整合数据...")
        
        new_payload = {
            "model": "deepseek-ai/DeepSeek-V3",
            "messages": messages,
            "temperature": 0.1 # 降低温度，防止瞎编
        }
        
        real_response = requests.post(url, headers=headers, json=new_payload)
        
        if real_response.status_code == 200:
            final_msg = real_response.json()["choices"][0]["message"]["content"]
            print("\n=== 最终回复 ===")
            print(final_msg)
        else:
            print(f"第二次请求失败，状态码: {real_response.status_code}")
    else: 
        print(f"\n[错误] 大模型试图调用本地不存在的函数：{function_name}")
else:
    print("\n大模型觉得不需要调用函数，直接给出了回答：")
    print(msg.get("content", ""))
