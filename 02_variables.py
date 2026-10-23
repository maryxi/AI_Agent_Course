# 创建变量
# player_name = "小马"
# level = 99

# print(player_name)
# print(level)

num_1 = 10
num_2 = 20
print("数字相加结果：", num_1 + num_2)

str_1 = "10"
str_2 = "20"
print("字符串相加结果：", str_1 + str_2)

# 类型转换
# int()
api_result = '100'
api_result1 = '200'
print(int(api_result) + int(api_result1))

float() 
str()

'''
# 课后练习：
# 1. 创建一个变量保存角色的名字（字符串）
# 2. 创建一个变量保存角色的血量（数字）
# 3. 角色受到攻击，血量减少 20，打印出角色受击后的血量。
# 附加题：如果受到的攻击伤害是一个字符串 "20"，你应该怎么处理？
'''


num1 = 11
num2 = 11.61
print("数字11宽度限制5: %5d" % num1)
print("数字11.22宽度限制7，小数精度3: %7.1f" % num2)

# name ="resr1"
# year = 100

# print(f"{name}, {year}hahah ")

# print("1*1的结果： %d:" % (1* 1))
# print(f"zifuchuande leixing {type(name)}" )

# name ="公司"
# stock_price = 10
# stock_code = 11
# stocke_price_daily = 1.2
# growth_day = 12

# print(f"公司{name}，股票代码{stock_code}，当前股价{stock_price}")
# print("每日增长系数：%.1f, 经过%d的增长，股价达到%.2f" %(stocke_price_daily, growth_day, stock_price* stocke_price_daily**growth_day))

# print("who")
# name = input("sho?")
# print(f"hello {name}")

# tall = input("身高是：")
# # age = 15
# if int(tall) >=130:
#     print("超高")
# else:
#     print("没有超高")



# tall = int(input("身高是："))
# vip_level = int(input("vip等级是："))
# if tall < 130:
#     print("超高, 不免费")
# elif vip_level > 1:
#     print("免费")
# else:
#     print("不免费")


# tall = int(input("身高是："))
# vip_level = int(input("vip等级是："))
# if tall >= 130:
#     print("超高, 不免费, 但是vip等级大于1可以免费")
#     if vip_level > 1:
#         print("免费")
#     else:
#         print("不免费")
# else:
#     print("不免费")

# 参数字
import random

num = random.randint(1, 10)

guessNum = int(input("参数字"))

if guessNum == num:
    print("恭喜你猜对了")
else:
    if (guessNum > num):
        print("你猜的数字大了")
    else:
        print("你猜的数字小了")
    
    guessNum = int(input("参数字"))
    if guessNum == num:
        print("恭喜你猜对了")
    else:
        if (guessNum > num):
            print("你猜的数字大了")
        else:
            print("你猜的数字小了")

        guessNum = int(input("参数字"))
        if guessNum == num:
            print("恭喜你猜对了")
        else:
            if (guessNum > num):
                print("你猜的数字大了")
            else:
                print("你猜的数字小了")


