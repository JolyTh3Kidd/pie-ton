def rta(a, b):
    return (a * b) / 2

def rectangle_area(a, b):
    return a * b

def main():
    x, y, z, t = map(float, input().split())
    area = rta(x, y) + rectangle_area(z, t)
    print(area)

main()
