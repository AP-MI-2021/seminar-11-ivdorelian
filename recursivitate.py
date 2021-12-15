def search(lst, v):
    """
    return True daca v se afla in lst si False altfel
    :param lst:
    :param v:
    :return:
    """
    if not lst:
        return False

    if v == lst[0]:
        return True

    return search(lst[1:], v)


print(search([5,2,6,7,2,1,12,4,3,2,1,3,5,67], 15))


def my_filter(lst, fun):
    #return [x for x in lst if fun(x)]
    if not lst:
        return []

    if fun(lst[0]):
        return [lst[0]] + my_filter(lst[1:], fun)
    return my_filter(lst[1:], fun)


print(my_filter(list(range(100)), lambda x: x % 2 == 0))


def get_min(lst):
    if len(lst) == 1:
        return lst[0]

    t = get_min(lst[1:])
    if lst[0] > t:
        return t
    return lst[0]


print(get_min([4,6,3,1,5,7,8,-3,-7,-4,234,-67,234,23]))


def hanoi(n, A, B, C):
    """
    muta n discuri de pe A pe C folosind B ca intermediar
    :param n: nr de discuri
    :param A: stalpul sursa
    :param B: stalpul intermediar
    :param C: stalpul destinatie
    :return: afiseaza mutarile
    """
    if n == 1:
        print(f'{A} -> {C}')
        return

    hanoi(n - 1, A, C, B)
    print(f'{A} -> {C}')
    hanoi(n - 1, B, A, C)


hanoi(3, 'a', 'b', 'c')
