def rectangle_area(a, b):
    return a * b

def triangle_area(a, h):
    return (a * h) / 2

def circle_area(r):
    return 3.14 * r * r

def main():
    a = float(input())
    b = float(input())
    r = float(input())
    print(rectangle_area(a, b))
    print(triangle_area(a, b))
    print(circle_area(r))

main()
