#Purpose: This exercise introduces you to the fundamental building blocks of 
#working with tuples: creating them, retrieving individual elements using index positions,
# and measuring their size using len(). These are the first skills you need
#  before working with any tuple-based data.

my_tuple = ("Deepashri", 5, 8, 3.5, True, 60)
          #   0          1  2    3   4     5 
#print(type(my_tuple))
print("index 0 ", my_tuple[0][8])
print("index 1 ",my_tuple[1])
print("index 2 ",my_tuple[2])
print("index 3 ",my_tuple[3])
print("index 4 ",my_tuple[4])
print("index 5 ",my_tuple[5])

print("Size of my tuple is",len(my_tuple))


for t in my_tuple:
    print("my values are:", t)