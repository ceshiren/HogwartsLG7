# 通过class 关键字定义一个类
class House:
    # 类的属性（静态属性）
    door = ""
    floor = ""
    # 类的方法
    # 使用def 定义函数， 类中的函数叫做（动态）方法
    def cook(self):
        print("我在厨房炸鸡排")

    def sleep(self):
        print("我在卧室睡觉")
# 实例对象
bob_house = House()
bob_house.door = "white"
bob_house.floor = "black"
# 可以使用debug 的方式，查看实例的属性内容
# 可以定义多个实例对象
# 修改实例的属性不会影响类本身
print("house.door对应的值为",House.door)
# 修改当前实例的属性不会影响到其他的实例
mary_house = House()
print(mary_house)


