def main():
    n = int(input())
    s = oct(n)[2:]
    print(s.zfill(10))

main()
