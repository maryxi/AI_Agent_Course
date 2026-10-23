# 列表 List

# 今天的内容主要分为四个部分：
# 1. 列表的定义与特点 ：什么是列表，它能存什么。
# 2. 下标索引 ：如何精准定位列表中的某一个数据。
# 3. 列表的内置操作 ：如何对列表进行增、删、改、查。
# 4. 列表的遍历 ：如何用循环把列表里的数据挨个取出来。

# my_list = ["Python", 100, [1, 2]]
# print(my_list[0])
# print(my_list[-1])

# 3. 列表的操作
data = ["A", "B"]

# 【添加元素】
data.append("C")          # append: 在末尾追加 1 个元素
data.extend(["D", "E"])   # extend: 在末尾追加多个元素（传入一个列表）
data.insert(1, "X")       # insert: 在索引为 1 的位置，插入 "X"

# 【删除元素】
data.pop()                # pop: 默认删除并返回最后一个元素
data.remove("A")          # remove: 删除第一个匹配到的 "A"
del data[0]               # del: 删除指定索引位置的元素
# data.clear()            # clear: 清空整个列表的所有元素

# 【查询与统计】
print(data.count("X"))    # count: 统计 "X" 出现的次数
print(data.index("B"))    # index: 返回 "B" 第一次出现的索引位置
print(len(data))          # len: 返回列表的长度（元素个数）

for i in items:
    print(i)

index = 0
while index < len(items):
    print(items[index])
    index += 1