# 字典 Dict

# 1、怎么创建字典
# 2、字典的 3 大铁律是什么
# 3、怎么对字典进行增、删、改、查
# 4、字典的遍历

# my_dcit = {"name":"张三", "age":18, "gender":"男", test: {
#     "name":"张三",
#     "age":18,
#     "gender":"男"
# }}

# empty_dict = {}
# empty_dict = dict()


my_dict = {"name": "周杰伦", "song": "七里香"}
# print(my_dict["song"])

my_dict["song"] = "夜曲"
# print(my_dict["song"])

my_dict["age"] = 40
# print(my_dict["age"])
# deleted_value = my_dict.pop("age")
# print(deleted_value)
# print(my_dict)

# print(my_dict.keys())
# print(len(my_dict))
# my_dict.clear()
# print(my_dict)

for key in my_dict:
    print(f"key: {key}, value: {my_dict[key]}")