def quick_sort(l: list):
    def sort(start: int, end: int):
        print(str(start) + ' ' + str(end))
        if start == end:
            return
        middle = start
        for i in range(start + 1, end):
            if l[i] < l[middle]:
                l[i], l[middle] = l[middle], l[i]
                middle = i
        print(l)
        sort(start, middle)
        sort(middle + 1, end)
    sort(0, len(l))

if __name__ == "__main__":
    l = [3, 56, 31, 17, 6, 8, 11, 3]
    quick_sort(l)
    print(l)
