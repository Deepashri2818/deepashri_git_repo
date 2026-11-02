marks = int(input("Enter your marks: "))

if marks in range(76, 101):
    print("Grade A")
elif marks in range(51, 76):
    print("Grade B")
elif marks in range(26, 51):
    print("Grade C")
elif marks in range(0, 26):
    print("Grade D")
else:
    print("Invalid marks")