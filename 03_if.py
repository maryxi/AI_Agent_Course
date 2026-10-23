# hp = 0 # 生命值
# if hp <= 0:
#     print("没血了，游戏结束！")
# else:
#     print("存活中，还能继续战斗！")

# elif -> else if


# hp = 100 # 生命值
# if hp <= 0:
#     print("没血了，游戏结束！")
# elif hp < 50:
#     print("血量低了，需要回城！")
# else:
#     print("存活中，还能继续战斗！")


# 课后练习：简单的密码验证器
# 1. 创建一个变量 password，随便赋值一个密码（比如 "123456"）。
# 2. 假设正确的密码是 "888888"。
# 3. 写一段 if/else 判断：如果密码对，打印“欢迎回家”；如果不对，打印“密码错误，拒绝访问”。

# print("请输入密码：")
# password = input("请输入密码：")

# import random 
# num = random.randint(1, 10)
# print(num)
# gussNum = input("请输入你猜的数字：")

# if num == gussNum:
#     print("恭喜你猜对了！")
# else:
#     print("很遗憾，你猜错了。")
#     guessNum = input("请重新输入你猜的数字：")
#     if guessNum == num:
#         print("恭喜你猜对了！")
#     else:
#         print("很遗憾，你猜错了。")

# sum = 0
# i = 1
# while i<= 100:
#     sum += i
#     i += 1

# print(sum)

# # 课后练习：猜数字游戏
# import random

# count = 0
# num = random.randint(1, 100)
# flag = True
# while flag:
#     guessNum = int(input("请输入你猜的数字："))
#     count += 1

#     if num == guessNum:
#         print("yes!")
#         flag = False
#     else:
#         print("no!")
#         if guessNum > num:
#             print("你猜的数字太大了")
#         else:
#             print("你猜的数字太小了")
# print(f"你猜了{count}次")


# i = 1

# while i<= 100:
#     print(f"当前数字是{i}")

#     j = 1

#     while j <= 10:
#         print(f"hua{j}")
#         j += 1
#     i+=1

# 乘法口诀表
# i = 1

# while i< 10:
#     j = 1
#     while j <= i:
#         print(f"{j} * {i} = {i * j}\t", end = '')
#         j += 1
#     i += 1
#     print()

# str = "a2aafff11a"
# count = 0
# for i in str:
#     if i == "a":
#         count += 1
# print(count)


# num = 100
# count = 0

# for i in range(num):
#     if i % 2 == 0:
#         count  += 1

# for i in range(1,10):
#     for j in range(1, i+1):
#         print(f"{j} * {i} = {j * i}\t", end ='')
#     print()

# def my_count(data):
#     count = 0
#     for i in data:
#         count += 1

#     print(count)

myList = ["a","b","c","d","e"]
# print(myList.index("c"))
# myList[0] = "A"
# print(myList)

# myList.insert(2, "C")
# print(myList)

# myList.append(33)
# print(myList)

# myList.extend([44,55])
# print(myList)


# del myList[-2]
# myList.pop(2)
# myList.remove("b")
# print(myList)


# longList = [1,2,3,4,5]
# newLsit = []
# for i in range(len(longList)):
#     if longList[i] % 2 == 0:
#         newLsit.append(longList[i])
# print(newLsit)

mystr = "hha 11 dd"
mystr.count("h")
mystr.replace(" ","|")


