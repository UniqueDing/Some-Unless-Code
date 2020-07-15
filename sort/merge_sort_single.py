def merge_sort(l: list):
    def sort(start: int, end: int):
        middle = int((end - start) / 2 + start)
        if end - start > 1:
            sort(start, middle)
            sort(middle + 1, end)
        if end == start:
            return

        p = start
        q = int((end - start) / 2 + start) + 1
        templ = []
        while True:
            if p > middle:
                templ += l[q:end+1]
                break
            if q > end:
                templ += l[p:middle+1]
                break
            if l[p] < l[q] and p <= middle:
                templ.append(l[p])
                p += 1
                continue
            if l[p] >= l[q] and q <= end:
                templ.append(l[q])
                q += 1
                continue
        l[start:end+1] = templ
        print(l[start:end+1])
        return

    sort(0, len(l)-1)
    # sort(4, 5)


if __name__ == "__main__":
    l = [4, 19, 44, 53, 6, 21, 9, 77, 5, 15, 109, 5]
    merge_sort(l)
    print(l)
