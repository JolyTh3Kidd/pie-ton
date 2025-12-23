def main():
    s1 = input()
    s2 = input()
    if len(s1) != len(s2):
        print("NO")
        return
    count1 = {}
    count2 = {}
    for c in s1:
        count1[c] = count1.get(c, 0) + 1
    for c in s2:
        count2[c] = count2.get(c, 0) + 1
    if count1 == count2:
        print("YES")
    else:
        print("NO")

main()
