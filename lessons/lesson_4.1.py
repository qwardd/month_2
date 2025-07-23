class Animal:
    def speak(self):
        print("Animal is speaking")

class Cat(Animal):
    def speak(self):
        super().speak()
        print("мяу мяу")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Гав гав")

class CatDog(Dog, Cat):
    def speak(self):
        super().speak()
        print("мяугав ")

kotopes = CatDog()
kotopes.speak()
print(CatDog.mro()) # Method resolution order
print(Dog.mro())
# diamond problem - проблема выбора порядка вызова метода
# при множественном наследовании

class Circle:
    # переменные класса
    pi = 3.1415
    count = 0

    def __init__(self, radius):
        # переменная экземпляра класса
        self.radius = radius

    @classmethod
    def get_count(cls):
        return cls.count

    @staticmethod
    def add_numbers(a, b):
        print(Circle.pi * a)
        return a + b


print(Circle.pi)
print(Circle.count)
print(Circle.add_numbers(2, 3))