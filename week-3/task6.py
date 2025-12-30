def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def main():
    a, b = map(int, input().split())
    g = gcd(a, b)
    l = (a * b) // g
    print(g, l)

main()
