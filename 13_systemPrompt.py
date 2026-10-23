import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.siliconflow.cn/v1")

system_instruction = """
你是一个极其严厉的 Python 高级架构师。
任务：审核用户提交的 Python 代码问题。
约束：
1. 必须先用非常刻薄、高傲的语气指出用户的低级错误。
2. 嘲讽结束后，必须给出完全正确、优雅的代码解决方案。
3. 绝对不要说“你好”、“很高兴为您解答”等废话。
输出格式要求：
必须严格分为两部分：
【架构师的嘲讽】：(填入嘲讽内容)
【优雅的代码】：(填入正确的代码)
"""

response = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V3",
    messages=[
        {"role": "system", "content": system_instruction},
        {"role": "user", "content": "老师，我用 while 循环去遍历字典，为什么一直报错啊？"},
    ],
    stream=False,
    reasoning_effort="high",
    extra_body={"thinking": {"type": "enabled"}}
)

print(response.choices[0].message.content)