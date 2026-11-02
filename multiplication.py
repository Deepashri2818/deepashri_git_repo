num = int(input("Enter number:"))
print("Multiplication of number", num)
total = 0
for i in range(1, 11):
    total = num * i
    print(num, "*", i, "=", total)
