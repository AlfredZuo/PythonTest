class Cat:
    def eat(self):
        print("小猫爱吃鱼")
        pass

    def drink(self):
        print("小猫要喝水")


tom = Cat()
tom.eat()
tom.drink()
print(tom)
addr = id(tom)
print("%d" % addr)
print("%x" % addr)
