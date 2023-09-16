def get_map_from_list(data, exctract_func):
    result = {}
    for elem in data:
        key = exctract_func(elem)
        result[key] = result.get(key, []) + [elem]
    return result
