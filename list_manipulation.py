#Change Element: Change the second element of a list to 200 and print the updated list.
#Append Element: Add 600 o the end of a list and print the new list.
#Insert Element: Insert 300 at the third position (index 2) of a list and print the result.
#Remove Element (by value): Remove 600 from the list and print the list.
#Remove Element (by index): Remove the element at index 0 from the list print the list.

my_list = [25, 50, 60, 56, 99]
#          0    1   2   3   4
print()
print("List before change is", my_list)
my_list[2] = 200
print("List after change is", my_list)

print()
my_list.append(600) 
print("List after adding element is", my_list)

print()
print("List before change is", my_list)
my_list[2] = 300
print("List after changing third position (index 2)"  , my_list)

print()
print("List before change is", my_list)
my_list.remove(600)
#my_list.pop(600)
print("List after removing 600 from the list (by value)"  , my_list)

print()
print("List before change is", my_list)
my_list.pop(0)
print("List after removing the element at index 0 (by index)"  , my_list)