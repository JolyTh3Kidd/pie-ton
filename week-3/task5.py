def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def main():
    A, B, C, D = map(int, input().split())
    n = A * D - B * C
    d = B * D
    g = gcd(abs(n), d)
    print(n // g, d // g)

main()
