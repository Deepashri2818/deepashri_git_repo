num1 = int(input("Enter number1:"))
num2 = int(input("Enter number2:"))
num3 = int(input("Enter number3:"))

if num1 > num2 and num1 > num3:
    print("Num1 is greater among all")
elif num2 > num1 and num2 > num3:
    print("Num2 is greater among all")
else:
    print("Num3 is greater among all")