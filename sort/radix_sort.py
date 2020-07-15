def radix_sort(l: list, radix: int = 10):
    temp_radix = radix
    b = [[] * x for x in range(radix)]
    while True:
        b = [[] * x for x in range(radix)]
        for i in l:
            temp = int(i / (temp_radix / radix)) % radix
            b[temp].append(i)
        if len(b[0]) == len(l):
            break
        l.clear()
        for i in b:
            l += i
        temp_radix *= radix
        print(b)


if __name__ == "__main__":
    l = [6, 11, 45, 124, 6, 64, 86, 746, 31, 9, 5, 438]
    radix_sort(l, 8)
    print(l)
