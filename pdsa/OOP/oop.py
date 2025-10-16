# oop inpython 
class dog:
    def dog(self,name ,age ,rollnumber):
        self.l = name
        self.a = age 
        self.r = rollnumber
    def display(self , mujo):
        print(f",My name is {self.l} and my mujo is {mujo}")

# constructor
result =dog("lelisa",12,44)
result.display("kena")
#---------------------------------
class total:
    def add(self , a,b):
        print("the sum is:",a+b)

t = total()
t.add(12,33)
#----------------------------

class Car:
    def __init__(self,model):
        self.model = model
    
    def setPrice(self ,price):
        self.price = price 

    def getPrice(self):
        return self.price
    
car = Car("marchedes")
car.setPrice(10101010)

print(car.model ,"and the price is: ",car.getPrice())
    

# using class lets us print name and age

class Person:
    def __init__(self, name ,age =22,value = 12 ):
        self.name = name
        self.age = age
 


person = Person('John',23)
print(f"I'm {person.name}. I'm {person.age} years old.")

# using class creating  values

class naming:
    def haha(self ,*kena):
        if len(kena) == 3:
            return True 
        return False 
   
name = naming()
print(name.haha(1,2))
 
class Person:
    def __init__(self, *args, **kwargs):
        if len(args) == 1:
            self.name = args[0]
            self.age = kwargs.get('age', None)
        elif len(args) == 2:
            self.name, self.age = args
        else:
            self.name = kwargs.get('name', 'Unknown')
            self.age = kwargs.get('age', 0)

p1 = Person("Alex")
p2 = Person("Alex", 25)
p3 = Person(name="John", age=20)

print(p1.__dict__)
print(p2.__dict__)
print(p3.__dict__)

# concept of inheritance 

class Person:
     
    def __init__(self,name,age):
        self.n = name 
        self.a = age 
    
    def greet(self):

        return f"hi my beloved {self.n} "
    

class Employe(Person):

    def __init__(self,name ,age ,role):
        super().__init__(name, age) 
        self.role = role 

    def greet(self):
        return  super().greet()+f"your role in here is{self.role}" 

e = Employe("zara",12,"googledevloper")

print(e.greet())

# understanding the difference b/n the class variable and the instance variable 
'''These are the variables that are shared across all instances of a class. 
It is defined at the class level, outside any methods'''
