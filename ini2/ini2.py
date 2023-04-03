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
                + ' = ' + str(num) + ' must be less than 1000!'
        super().__init__(message)


def ini2(a, b, path=None, save=False):
    # assert a > 0, f'Error: a = {a} must be positive!'
    # assert b > 0, f'Error: b = {b} must be positive!'

    # assert a < 1e3, f'Error: a = {a} must be less than 1000!'
    # assert b < 1e3, f'Error: b = {b} must be less than 1000!'
    
    if a <= 0:
        raise _NumberNegativeValueError(a)
    if b <= 0:
        raise _NumberNegativeValueError(b)

    if a >= 1e3:
        raise _NumberOverflowError(a)
    if b >= 1e3:
        raise _NumberOverflowError(b)
    
    result = a*a + b*b

    if save:
        if path is None:
            path = os.path.join(os.path.dirname(os.path.realpath(__file__)), \
                                'rosalind_ini2_1_output.txt')
        else:
            path = os.path.join(path, 'rosalind_ini2_1_output.txt')
        with open(path, 'w') as file:
            file.write(str(result))

    return result


if __name__ == '__main__':
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), \
                           'rosalind_ini2_1_dataset.txt'), 'r') as file:
        a, b = list(map(int, file.readline().split()))

    print(a, b)
  
    print(ini2(a, b, save=True))
