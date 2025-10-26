print("Jesus is lord.")

'''what we have seen so far 
1.class creation and object instantiation 
2.self parameter 
3.__init__ method 
4. class and instance variable 
5. inheritance in oop:it allows to 
'''

class Dog:
    def __init__(self,name ):
        self.name = name 

    def dispalay_name(self,jajc):
        print(f"the name of the dog is {self.name } and {jajc}.")
    
    def lel(self):
        print(self.name )
class TypeOneDog(Dog):
    def sound(self):
        print("sounds woof!!")

c= TypeOneDog("jen")
w = TypeOneDog("kna")
print(c.sound())

class Animal:
    def __init__(self , name ,age ):
        self.name = name 
        self.age = age 

    def display(self , sound ):
        print(f"name of the dog:{self.name }")
        print(f"age of the dog:{self.age}")
        print(f"the dog sound:{sound}")

class life:
    def __init__(self,longness):
        self.l = longness
    def check(self):
        print("yes ofcourse. ")


class dog(Animal,life):
    def display(self , sounding):
        print(f"the sound of the dog is:{sounding}")
        super().check()

c = dog("kak",4,"kakakak")
c.display("woof woof")

class Animal:
    def __init__(self,name):
        self.name = name 
       
    def info(self ):
        print(f"animal name:{self.name }")

class Dog(Animal):
    
    def __init__(self,name ,breed ):
        super().__init__(name)
        self.breed = breed 

    def details(self):
        print(self.name , " is a ",self.breed )


d = Dog("jak","kiwi")
d.details()

class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):  
    def show_role(self):
        print(self.name, "is an employee")

class Manager(Employee):  # Manager inherits from Employee
    def department(self, dept):
        print(self.name, "manages", dept, "department")

mgr = Manager("")
mgr.show_role() 
mgr.department("HR")

class Dog:
    sound = "bark"
    def whattodo(self,name ,sound):
        print(f"the job of my dog called {name} is {sound}")
    
# Creating object from class
Dog().whattodo("kit","bark") # Accessing the class

s = True 
dir(s)