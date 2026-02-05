##Class and Objects
class Car:
    color="Blue"
    brand="BMW"
car1=Car()
print(car1.color)
print(car1.brand)

class Student:
    def __init__(self):
        print(self)#address of the obj self is pointing
        print("Adding a name")
s1=Student() 
print(s1)
#u can write self as anything like abcd

#instead:
class Student:
    college_name="Montessori"
    def __init__(self, name=None, marks=None):
        if name is None and marks is None:
            print("default")
        else:
            self.name=name
            self.marks=marks
    #class can have only one init, if 2 then last written one will be executed
    # def __init__(self):
    #     print("its default")
    
s2=Student("Aniketh","12")
print(s2.name)
print(Student.college_name)

##class Attributes
class Student:
    college_name="Montessori"
    name="Anonymous"
    
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks

s1=Student("Aniketh", 12)
print(s1.name) #obj.atr>class.atr
print(Student.name)#can be called by class.atr

s1=Student("Aniketh", 12) 
print(s1.name, s1.marks)

##methods
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def greeting(self):
        print("Good Morning!")
    def get_marks(self):
        return self.marks
s1=Student("Aniketh",24)
s1.greeting()
print(s1.get_marks())

#Exercise 1
class Student:
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks
    @staticmethod #decorator
    #defn: wrap functions or methods for enhanced functionality
    def hello():
        print("Hello")
    def calAvg(self):
        sum=0
        for i in self.marks:
            sum+=i
        print("Avg marks of", self.name, "is", sum//3)
s1=Student("Aniketh",[100,100,99])
s1.calAvg()
Student.hello()
s1.name="Abhi"
s1.calAvg()

#Output1
# Avg marks of Aniketh is 99
# Hello
# Avg marks of Abhi is 99

#Exercise 2
class Bank:
    def __init__(self,bal,acc):
        self.bal=bal
        self.acc=acc
    def getBalance(self):
        return self.bal
    def debit(self):
        amt=int(input("Amout to be debited "))
        self.bal-=amt
        print("Debited: Rs",amt)
        print("Balance: Rs",self.bal)
    def credit(self):
        amt=int(input("Amout to be credited "))
        self.bal+=amt
        print("Credited: Rs",amt)
        print("Balance: Rs",self.bal)
acc1=Bank(2000,12345)
print(acc1.bal)
acc1.debit()
acc1.credit()
print("Succesfully finished")
#output2
# 2000
# Amout to be debited 1200
# Debited: Rs 1200
# Balance: Rs 800
# Amout to be credited 2000
# Credited: Rs 2000
# Balance: Rs 2800


        
        