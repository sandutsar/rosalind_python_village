import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), \
                             os.pardir))
from exceptions import NumberValueError

def ini4(a, b, path=None, save=False):
    result = 0

    # assert isinstance(a, int), f'Error: type(a) = {type(a).__name__} must be int!'
    # assert isinstance(b, int), f'Error: type(b) = {type(b).__name__} must be int!'

    # assert a > 0, f'Error: a = {a} must be > 0!'
    # assert b > 0, f'Error: b = {b} must be > 0!'

    # assert a < 1e4, f'Error: a = {a} must be < 10000!'
    # assert b < 1e4, f'Error: b = {b} must be < 10000!'

    if not isinstance(a, int):
        raise TypeError(f'Error: type(a) = {type(a).__name__} must be int!')
    if not isinstance(b, int):
        raise TypeError(f'Error: type(b) = {type(b).__name__} must be int!')

    if a <= 0:
        raise NumberValueError(num=a, sign='>', value=0)
    if b <= 0:
        raise NumberValueError(num=b, sign='>', value=0)
    
    if a >= 1e4:
        raise NumberValueError(num=a, sign='<', value=int(1e4))
    if b >= 1e4:
        raise NumberValueError(num=b, sign='<', value=int(1e4))
    
    assert a < b, f'Error: a = {a} must be < b = {b}!'

    for num in range(a, b + 1):
        if num % 2 != 0:
            result += num

    if save:
        if path is None:
            path = os.path.join(os.path.dirname(os.path.realpath(__file__)), \
                                'rosalind_ini4_1_output.txt')
        elif os.path.isdir(path):
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
