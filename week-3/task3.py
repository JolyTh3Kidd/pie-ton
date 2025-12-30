def gipotenuza(a, b):
    return (a * a + b * b) ** 0.5

def main():
    a1, b1 = map(float, input().split())
    a2, b2 = map(float, input().split())
    h1 = gipotenuza(a1, b1)
    h2 = gipotenuza(a2, b2)
    if h1 > h2:
        print("First is greater")
    elif h1 < h2:
        print("Second is greater")
    else:
        print("Equal")

main()
