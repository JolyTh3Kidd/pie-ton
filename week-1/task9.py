ticket = input("Enter a 6-digit number: ")
firstSum = sum(map(int, ticket[:3]))
lastSum = sum(map(int, ticket[3:]))

if firstSum == lastSum:
    print("Yes")
else:
    print("No")