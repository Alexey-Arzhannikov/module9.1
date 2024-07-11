int_list = [6, 20, 15, 9]


def apply_all_func(int_list, *function):
    results = []
    func = []
    dct = {}
    for i in function:
        results.append(i(int_list))
        func.append((i.__name__))
    for j in range(len(func)):
        key = func[j]
        value = results[j]
        dct[key] = value
    print(dct)


apply_all_func(int_list, max, min)
apply_all_func(int_list, len, sum, sorted)
