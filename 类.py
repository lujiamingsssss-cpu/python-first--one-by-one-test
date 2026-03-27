class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eat(self):
        print(self.name + "正在吃饭")
    def sleep(self): 
        print(self.name + "正在睡觉")
    def ag(self,told):
        print(self.name + "的年龄是" + str(self.age) + told)
p1 = Human("小明", 20)
p1.eat()
p1.sleep()
p1.ag(",is good time")
print(p1.name)