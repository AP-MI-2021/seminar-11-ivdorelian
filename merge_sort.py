from timeit import default_timer
from random import randint


def merge(lst, st, m, dr):
    merged = []
    i = st
    j = m + 1
    while i <= m and j <= dr:
        if lst[i] < lst[j]:
            merged.append(lst[i])
            i += 1
        else:
            merged.append(lst[j])
            j += 1

    merged.extend(lst[i:m+1])
    merged.extend(lst[j:dr+1])
    lst[st:dr+1] = merged


def merge_sort(lst):

    def inner(lst, st, dr):
        if st < dr:
            m = st + (dr - st) // 2 # (st + dr) // 2
            inner(lst, st, m)
            inner(lst, m+1, dr)
            merge(lst, st, m, dr)

    inner(lst, 0, len(lst) - 1)
    return lst


def get_time(func, times=10):
    start = default_timer()
    for _ in range(times):
        lst = []
        for _ in range(100000):
            lst.append(randint(1, 50000))

        func(lst)
    end = default_timer()
    print(f'It took: {end - start} seconds.')


get_time(sorted)
get_time(merge_sort)

# lst = [3,9,342,12,321,123,664,2123,213,577,32,46,123,2,5]
# merge_sort(lst, 0, len(lst) - 1)
# print(lst)