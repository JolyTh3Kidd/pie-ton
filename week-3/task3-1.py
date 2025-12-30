def main():
    enter = input()
    words = enter.split()
    result = []
    for n in words:
        result.append("".join(sorted(n)))
    print(" ".join(result))

main()