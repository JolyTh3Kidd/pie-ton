salaries = list(map(int, input("Enter salaries, divide with space: ").split()))
print("The difference:", max(salaries) - min(salaries))