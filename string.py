a = "Deepashri"
    #012345678
b = 10

print("Int to str conversion is:", a + str(b))
print("print value with space:",a,b)

for i in a:
    print(i, end= "")
    
print()    

#print(f" My name is {a} and my age is {b}")
print("My name is %s and my age is %s" % (a,b))

print("Index value is:",a[2])