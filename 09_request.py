# python requests 库的使用:
# - 第三方库的安装： pip 与 requests 库介绍
# - 发送 GET 请求：从服务端获取数据
# - 发送 POST 请求：向服务端提交数据
# - Response 对象的解析：状态码与数据提取

import requests

# 这是一个专门用于测试 HTTP 请求的公共接口
url_get = "https://httpbin.org/get"

params = {
    "name": "zz",
    "age": "18"
}
print("正在发送请求")
response = requests.get(url_get, params=params)
print("状态码：", response.status_code)

url_post = "https://httpbin.org/post"

# POST 请求提交的数据通常放在请求体（Body）中，使用 data 或 json 关键字
# payload = {
#     "name": "zz",
#     "age": "18"
# }
# print("正在发送请求")

# response = requests.post(url_post, json=payload)

if response.status_code == 200:
    # 提取纯文本格式的响应内容
    # print("响应文本：", response.text)
    
    # 提取 JSON 格式的响应内容，并直接转换为 Python 的字典类型
    res_dict = response.json()
    print("响应内容：", res_dict)
    print("响应内容的参数：", res_dict["args"]["name"])
else:
    print("请求失败")