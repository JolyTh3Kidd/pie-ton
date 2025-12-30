def inside(x, y, a, b, r):
    return (x - a) ** 2 + (y - b) ** 2 <= r * r

def main():
    a, b, r = map(float, input().split())
    points = [tuple(map(float, input().split())) for _ in range(3)]
    count = 0
    for x, y in points:
        if inside(x, y, a, b, r):
            count += 1
    print(count)

main()
