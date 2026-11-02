a = lambda x, y, z : print(x + y + z)  #oneline operation
a( 1, 2, 3)

print("Write a Python program to square and cube every number in a given list of integers using Lambda")

my_list = [ 2, 4, 8, 10]
sq = list(map(lambda x : x**2, my_list ))
cube = list(map(lambda x : x**3, my_list ))

print("Square is ", sq)
print("Cube is ", cube)
print()
print()

print("Write a Python program to count the even and odd numbers in a given list of integers using Lambda.")
even_odd_list = [ 2, 3, 4, 5, 8, 10, 11, 13, 18]

even_count = list(filter(lambda x : x % 2 == 0 , even_odd_list ))
odd_count = list(filter(lambda x : x % 2 != 0 , even_odd_list ))

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
print()
print()

print("Write a Python program to add two given lists using map and lambda.")

list1 = [ 2, 4, 6]
list2 = [ 2, 4, 6]

add_list = list(map(lambda x, y : x + y, list1, list2))
print("Sum of two list is: ", add_list)


print("Write a Python program to sort tuples using Lambda.")

my_tuple = ( 50, 8,  2, 15, 18 , 4, 6, 8, 10)
#tuple_list = list(my_tuple)
#sort_tuple_list = sorted(tuple_list, key=lambda x: x)
sort_tuple_list = sorted(my_tuple, key=lambda x: x)
#print("SOrted tuple list", sort_tuple_list)
print("SOrted tuple ", tuple(sort_tuple_list))

