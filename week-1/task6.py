a = float(input("First number: "))
b = float(input("Second number: "))

def calculation(a, b):
    calc = input("Operation: ")
    if calc == "+":
        print(a + b)
    elif calc == "-":
        print(a - b)
    elif calc == "*":
        print(a * b)
    elif calc == "/":
        print(a / b)
    else:
        print("Wild, Try again")
        calculation(a, b)

calculation(a, b)