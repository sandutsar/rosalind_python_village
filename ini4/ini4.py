import os


class _NumberNegativeValueError(Exception):
    def __init__(self, num, message=None):
        if message is None:
            message = 'Error: ' + [name for name in globals() \
                                   if globals()[name] == num][0] \
                + ' = ' + str(num) + ' must be positive!'
        super().__init__(message)


class _NumberOverflowError(Exception):
    def __init__(self, num, message=None):
        if message is None:
            message = 'Error: ' + [name for name in globals() \
                                   if globals()[name] == num][0] \
                + ' = ' + str(num) + ' must be less than 10000!'
        super().__init__(message)


def ini4(a, b, path=None, save=False):
    result = 0

    assert a < b, f'Error: a = {a} must be less than b = {b}!'

    # assert a > 0, f'Error: a = {a} must be positive!'
    # assert b > 0, f'Error: b = {b} must be positive!'

    # assert a < 1e4, f'Error: a = {a} must be less than 10000!'
    # assert b < 1e4, f'Error: b = {b} must be less than 10000!'

    if a <= 0:
        raise _NumberNegativeValueError(a)
    if b <= 0:
        raise _NumberNegativeValueError(b)
    
    if a >= 1e4:
        raise _NumberOverflowError(a)
    if b >= 1e4:
        raise _NumberOverflowError(b)

    for num in range(a, b + 1):
        if num % 2 != 0:
            result += num

    if save:
        if path is None:
            path = os.path.join(os.path.dirname(os.path.realpath(__file__)), \
                                'rosalind_ini4_1_output.txt')
        else:
            path = os.path.join(path, 'rosalind_ini4_1_output.txt')
        with open(path, 'w') as file:
            file.write(str(result))

    return result


if __name__ == '__main__':
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), \
                           'rosalind_ini4_1_dataset.txt'), 'r') as file:
        a, b = list(map(int, file.readline().split()))

    print(a, b)
    
    print(ini4(a, b, save=True))
