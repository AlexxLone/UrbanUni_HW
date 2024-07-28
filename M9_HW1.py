def apply_all_func(int_list, *functions):
    result = dict()
    for function_ in functions:
        result.update({function_.__name__: function_(int_list)})
    return result


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
