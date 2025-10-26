print("Jesus is lord")

class ihaveobject: # creating class 
    var = "i am attribute of the class" # int attribute of the class 
    def __init__(self , name , age):
        self.n = name # attribute of the object we can access the using the object
        self.a = age   # and update them using the object also

    # instance method 
    def someex(self):
        grade =  "i am the local variable " #local variable 
    # class method
    @classmethod 
    def classing(cls,naming):
        cls.name = naming
        print(f"name of the class variable is {cls.name}")
        print("i am class method ")
    #static class 
    @staticmethod
    def stating():
        age_var = "local variable"
        print(" i am the static class ")

ob1 = ihaveobject("name","age") #creating object
print(ob1.n)
print(ob1.var )
print(ihaveobject.classing("naming"))

