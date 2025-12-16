A = float(input("Enter any float number: "))
integerPart = int(A)
fractionalPart = int(round((A - integerPart) * 100))

newNum = fractionalPart + integerPart / 100
print("Reversed:",newNum)
