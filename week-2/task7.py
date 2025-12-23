def main():
    items = input().split()
    freq = {}
    for item in items:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    print("Purchase frequency:")
    for k in freq:
        print(k + ": " + str(freq[k]))
    max_item = None
    max_count = 0
    for k in freq:
        if freq[k] > max_count:
            max_count = freq[k]
            max_item = k
    print("Most popular item: " + max_item)
    once = []
    for k in freq:
        if freq[k] == 1:
            once.append(k)
    print("Purchased once: " + " ".join(once))
    print("Sorted by frequency:")
    sorted_items = sorted(freq.items(), key=lambda x: -x[1])
    for k, v in sorted_items:
        print(k, v)

main()
