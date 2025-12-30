def rectangle_area(a, b):
    return a * b

def main():
    for _ in range(3):
        a, b = map(float, input().split())
        print(rectangle_area(a, b))

main()