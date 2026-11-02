# Exercise 10: Delete a List of Keys
print("Exercise 10")
dict_student = { "name": "Siya",  "Grades": 25 , "City": "Pune", "Pin": 411052}
print("Before Deleting", dict_student)

list_student = ["Grades", "Pin"]
for i in list_student:
    dict_student.pop(i)
print("After Deleting", dict_student)

print("**************************************")