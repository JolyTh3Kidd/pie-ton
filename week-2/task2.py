def is_cyclic(a, b):
    if len(a) != len(b):
        return False
    double_b = b + b
    return a in double_b
def main():
    a = input()
    b = input()
    count = 0
    len_b = len(b)
    for i in range(0, len(a) - len_b + 1):
        sub = a[i:i+len_b]
        if is_cyclic(sub, b):
            count += 1
    print(count)

main()
