def swap_array(arr, n):
    if n > 1:
        arr[0], arr[n - 1] = arr[n - 1], arr[0]

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(arr)
    swap_array(arr, n)
    print(arr)

main()
