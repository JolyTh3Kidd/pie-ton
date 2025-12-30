def triangle_area(a, h):
    return (a * h) / 2

def hexagon_area(a):
    h = (3 ** 0.5) * a / 2
    return 6 * triangle_area(a, h)

def main():
    a = float(input())
    print(hexagon_area(a))

main()
