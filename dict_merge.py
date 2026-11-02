## Exercise 5: Merge Dictionaries
print("Exercise 5")
student = {"Name": "Riya", "City": "Pune"}
marks =   {"Name": "Riya", "Grades": "56"}

print("Method1:")
student.update(marks)
print("Dict after merge1 is ", student)

print("Method2:")
merge_dict = {**student,**marks}
print("Dict after merge2 is ",merge_dict)

print("Method3:")
merge_dict = student | marks
print("Dict after merge3 is ",merge_dict)
print("**************************************")