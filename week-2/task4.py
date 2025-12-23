def main():
    n, m = map(int, input().split())
    text = input()
    words = set()
    i = 0
    while i <= n - m:
        words.add(text[i:i+m])
        i += 1
    print(len(words))

main()
