def heap_sort(l: list):
    def sort(num: int, node: int, flag: bool):
        # print(str(node) +' '+str(num))
        if num == len(l) - 1:
            return
        if node < 0:
            l[0], l[-(num) - 1] = l[-(num) - 1], l[0] #swap topest
            num += 1
            sort(num, int((len(l) - num) / 2) - 1, True)
            return
        if node * 2 + 1 < len(l) - num:
            if l[node] < l[node * 2 + 1]:
                l[node], l[node * 2 + 1] = l[node * 2 + 1], l[node]
                sort(num, node * 2 + 1, False)
        if node * 2 + 2 < len(l) - num:
            if l[node] < l[node * 2 + 2]:
                l[node], l[node * 2 + 2] = l[node * 2 + 2], l[node]
                sort(num, node * 2 + 2, False)
        if flag:
            sort(num, node - 1, True)
    sort(0, int(len(l) / 2) - 1, True) #last non-leaf


if __name__ == "__main__":
    l = [6, 1, 17, 4, 20, 15, 33, 10, 194, 54, 99, 1004, 5, 477]
    heap_sort(l)
    print(l)
