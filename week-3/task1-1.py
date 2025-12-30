def array_sum(arr):
    s = 0
    for x in arr:
        s += x
    mean = s / len(arr)
    return s, mean

def main():
    for _ in range(3):
        arr = list(map(int, input().split()))
        s, m = array_sum(arr)
        print(s, m)

main()
