import random
import copy


def monkey_sort(l: list):
    count = 0
    while True:
        temp_list = copy.deepcopy(l)
        sort_list = []
        for i in range(len(temp_list)):
            random_num = random.randint(0, len(temp_list) - 1)
            sort_list.append(temp_list[random_num])
            del temp_list[random_num]
        count += 1
        print(str(count) + ' ' + str(sort_list))
        if check(sort_list):
            return sort_list, count

def check(l: list):
    for i in range(len(l) - 1):
        if l[i] < l[i + 1]:
            return False
    return True
        
if __name__ == "__main__":
    l = [6, 35, 8, 49, 43, 106, 5, 13, 64, 97]
    result = monkey_sort(l)
    print('result ' + str(result[0]))
    print('count  ' + str(result[1]))
