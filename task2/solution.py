#first


def groupby(func, seq):
    keys = {func(x) for x in seq}
    result = {x: [] for x in keys}
    for key in keys:
        result[key] = [y for y in seq if key == func(y)]
    return result
#second


def compose(func_1, func_2, unpack=False):
    """
    compose(func_1, func_2, unpack=False) -> function

    The function returned by compose is a composition of func_1 and func_2.
    That is, compose(func_1, func_2)(5) == func_1(func_2(5))
    """
    if not callable(func_1):
        raise TypeError("First argument to compose must be callable")
    if not callable(func_2):
        raise TypeError("Second argument to compose must be callable")

    if unpack:
        def composition(*args, **kwargs):
            return func_1(*func_2(*args, **kwargs))
    else:
        def composition(*args, **kwargs):
            return func_1(func_2(*args, **kwargs))
    return composition


def iterate(func):
    curent_result = (lambda x: x)
    yield curent_result
    while True:
        curent_result = compose(curent_result, func)
        yield curent_result


#third


def zip_with(func, *iterables):
    if len(iterables) == 0:
        while True:
            yield func
    else:
        current_index = 0
        while True:
            params = []
            for x in iterables:
                if(len(x) > current_index):
                    params.append(x[current_index])
                else:
                    break
            if(len(params) < len(iterables)):
                break
            yield func(*params)
            current_index += 1
