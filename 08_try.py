# try/except

# 1、try-except 语法
# 2、怎么捕获所有类型的报错？
# 3、异常处理与 else 和 finally 的妙用
# 4、底层逻辑：异常的传递性

# print("hello world")
# try:
#     num = 1 /0
# except Exception as e:
#     print(f"捕获到异常：{e}")
# else:
#     print("没有异常")
# finally:
#     print("finally")
# print("end")

def worker():
    print("员工干活")
    1 / 0

def boss():
    try:
        worker()
    except Exception as e:
        print(f"板出面解决问题：员工犯了错: {e}")

boss()