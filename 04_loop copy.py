from curses import keyname


print("变出一只兔子")
# print("变出一只兔子")
# print("变出一只兔子")
# for while

# for i in [1,2,3]:
    # print(f"变出第{i}只兔子")

count = 3
while count > 0:
    print(f"倒计时：{count}")
    count -= 1
    for i in [1,2,3]:
        print(f"变出第{i}只兔子")



print("时间结束")


myset = set()
myList = [11, 33,22,11,33,44]

for i in myList:
    myset.add(i)
print(myset)

# 字典的关键
# 通过key找到value 存储的是键值对 key：value
# 空字段的定义 {} dict()
# 字段的key不能重复
# 没有下标索引
# 使用 []  来访问value dict[key]
# key、value可以是任意类型，key不可以是字典类型
# value可以为字典，就是字段嵌套字典
# 删除pop，可传参，传key，就删除key这个元素
#  修改obj[key] = 'xx' 新增同样（本身在字典里没有就是新增，否则就是修改）clear()清除字典 
# obj.keys() 获取所有的key 用来遍历
# 支持for循环 不支持while循环 因为没有下标索引
# len(obj) 获取字典的长度

countNum = 0
with open("test.txt", "r", encoding="utf-8" ) as f:
    content = f.read()
    countNum = content.count("it")
# 文件的read的读取是按照指针的 连续调用read方法是依稀往后读的

# 异常的捕获防止一行程序出现问题导致整个应用崩溃
# try except
# 多种类型的异常怎么捕获
# except Exception as e:
#     print(e)
# 后面可以接else 也有finally
# finally 无论是否有异常，都会执行
# 异常是有传递性的


# python的json模块用花
# json.dumps(data) 把字典转换为json字符串 如果需要中文，需要传参 ensure_ascii=False 是dumps的第二个参数，不用这个参数中文就是一个unnicode的字符
# json.loads(data) 把json字符串转换为字典

# from pycharts.charts import Map

# map = Map()
# data = [
#     ("中国", 100),
#     ("美国", 200),
#     ("日本", 300),
# ]
# map.add("地图", data)
# map.render()

# 表格可以用class 对象类来实现
class Student:
    name = None
    age = None
    score = None

    def hello(self): #self 是对象本身 是必须传的，其他参数随意传 可以不传也可以传
        # self 是对象本身，可以调用对象的属性和方法
        print(f"hello world {self.name}")

stu1 = Student()
stu1.name = 'xiaoma'
stu1.age = 18
stu1.score = 90
stu1.hello()
print(stu1.name)
print(stu1.age)
print(stu1.score)
# 类里面有两类 就是属性和行为（方法）

class Student:
    name = None # 可以省了
    age = None
    score = None

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
        print(f"初始化学生 {self.name} {self.age} {self.score}")

stu = Student("xiaoma", 18, 90)
# 类里的魔术方法
# __init__ 初始化方法
# __str__ 字符串方法
# __lt__ 小于号方法
# __gt__ 大于号方法
# __eq__ 等于号方法
# 私有成员变量和方法 前面加上__ 定义
# 私有成员的变量和方法只能在类内部调用
# 外部不能直接调用

类的继承
# class Student(Person): #单继承模式 Student 是Person的子类

# 多继承模式 Student(Person, Teacher) 继承多个父类
# 子类能覆写父类的方法 就是重新定义同名的方法和属性
# 覆写之后如果还想调用父类的方法，需要在子类的方法里调用父类的方法
# 调用父类的其他方法
# super().方法名()
# 调用父类的属性
# super().属性名
# 或者用父类的名字.属性名
# Parent.属性名 Parent.方法名(self)

class AC:
    def cool(self):
        pass
class Medeia(AC):
    def cool(self):
        print("美的空调")

# class
md = Medeia()