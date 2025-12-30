def triangle_area(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5

def main():
    a, b, c, d, diagram = map(float, input().split())
    area = triangle_area(a, b, diagram) + triangle_area(c, d, diagram)
    print(area)

main()
