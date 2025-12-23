def main():
    valid_letters = set("ABCEHKMOPTXY")
    n = int(input())
    for _ in range(n):
        s = input()
        ok = True
        if len(s) != 6:
            ok = False
        else:
            if s[0] not in valid_letters:
                ok = False
            if not s[1:4].isdigit():
                ok = False
            if s[4] not in valid_letters or s[5] not in valid_letters:
                ok = False
        if ok:
            print("Yes")
        else:
            print("No")

main()
