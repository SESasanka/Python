# class myClass:
#     x = 5

# p1 = myClass()
# print(p1.x)

# class person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# class location:
#     def __init__(self,location):
#         self.location = location
    
# p1 = person("Sasanka",19)
# p2 = location("Kalagedihena")
# print(p1.name)
# print(p1.age)
# print(p2.location)


# class Engine:
#     def start(self):
#         print("Engine Started.")

# class Car:
#     def __init__(self):
#         self.engine = Engine()

#     def start_car(self):
#         self.engine.start()

# p1=Car()
# p1.start_car()

# class Person:
#     def __init__(self,name):
#         self.name = name

#     def greet(self):
#         return "Hello, " + self.name
    
#     def welcome(self):
#         message = self.greet()
#         print(message + " Welcome to our website")

# p1 = Person("Sasanka")
# p1.welcome()

class Animal:
    def sound(self):
        print("Animal makes a sound")
    
class Dog(Animal):
    def sound(self):
        print("Dogs barks")

p=Dog()
p.sound()