# - JSON 数据格式的定义与行业标准
# - Python 内置 json 库的序列化与反序列化
# - 实战：解析复杂嵌套的 API 响应数据（以天气数据为例）

import json
# json_str = '{"city": "Beijing", "temperature": 25, "is_raining": false}'
# print(type(json_str)) 

# parsed_dict = json.loads(json_str)
# print(parsed_dict)
# print(type(parsed_dict))

api_response = {
    "status": "success",
    "code": 200,
    "data": {
        "update_time": "2023-10-01 12:00",
        "forecast": [
            {"date": "10-01", "weather": "晴", "high": 28, "low": 15},
            {"date": "10-02", "weather": "多云", "high": 26, "low": 14},
            {"date": "10-03", "weather": "小雨", "high": 22, "low": 12}
        ]
    }
}

forecast = api_response["data"]["forecast"]
# print(forecast)

day_2 = forecast[1]
print(day_2)

high_temp = day_2["high"]
print(high_temp)

temp = api_response["data"]["forecast"][1]["high"]
print(temp)
