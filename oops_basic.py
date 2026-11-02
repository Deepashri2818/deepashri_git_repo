class A:
    a  = 22  #Attributes --> Class Attributes and Instance Attributes
    
    def m(self):
        print("Uncodemy")
        
#print(A.a)        
#A.m()  # Class attributes

#Declare object
#A() > CLass name
obj = A()
print(obj.a)
obj.m()  #gives error if self is not passed as parameter 
# Instance function - > Function has to be declared inside class
# self keyword as parameter 

