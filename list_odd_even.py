my_list = [10, 20, 30, 40, 50, 3, 7,99,55]

even_count = 0
odd_count = 0

for n in my_list:
    if n % 2 == 0:
        even_count = even_count + 1
        #print("Number is even")
    else:
        odd_count = odd_count + 1
        #print("Number is odd")
print("Even count is:", even_count)        
print("Odd count is:", odd_count)