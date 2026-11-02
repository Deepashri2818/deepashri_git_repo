a = {
    "Fname": "Deeps",
    "Age": 38
    
}

print("Dict is", a)
print("Name is",  a["Fname"])

a["Location"] = "Pune"  #add
print("Added location", a)  

del a["Age"] 
print("Deleted Age: ",a)

a["Fname"] = "Deepashri"
print("Updated name",a)
