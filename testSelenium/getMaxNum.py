def get_max_val(lst):
    '''Функция возвращает максимальное число из списка
    params: lst - List
    return max_val int'''
    for el2 in lst:
        max_val = el2
        for element in lst:
            if element > max_val:
                max_val = element
        return max_val

print(get_max_val([2, 3, 44]))

print(get_max_val([-10, -3, -2]))



