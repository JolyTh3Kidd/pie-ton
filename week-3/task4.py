def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def main():
    A, B, C, D = map(int, input().split())
    num = A * D
    den = B * C
    g = gcd(num, den)
    print(num // g, den // g)

main()
