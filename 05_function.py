# 函数是组织好的、可重复使用的、用来实现特定功能的代码段，提高代码的复用性，减少重复代码
# def 函数名(传入参数):
#     函数体
#     return 返回值

# def add(): # 形参
#     # print(a, b, c)
#     # return a + b +c

# result = add() # 实参
# print(result)

# def a():
#     print("a")

# def b():
#     print("b")
#     a()
#     print("b end")

# b()

num = 0
def fn():
    global num
    num = 10
    print(f"fn中的num是{num}")

fn()
print(f"外部num是{num}")
