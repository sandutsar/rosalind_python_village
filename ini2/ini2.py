import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), \
                             os.pardir))
from exceptions import NumberValueError

def ini2(a, b, path=None, save=False):
    # assert isinstance(a, int), f'Error: type(a) = {type(a).__name__} must be int!'
    # assert isinstance(b, int), f'Error: type(b) = {type(b).__name__} must be int!'

    # assert a > 0, f'Error: a = {a} must be > 0!'
    # assert b > 0, f'Error: b = {b} must be > 0!'

    # assert a < 1e3, f'Error: a = {a} must be < 1000!'
    # assert b < 1e3, f'Error: b = {b} must be < 1000!'
    
    if not isinstance(a, int):
        raise TypeError(f'Error: type(a) = {type(a).__name__} must be int!')
    if not isinstance(b, int):
        raise TypeError(f'Error: type(b) = {type(b).__name__} must be int!')

    if a <= 0:
        raise NumberValueError(num=a, sign='>', value=0)
    if b <= 0:
        raise NumberValueError(num=b, sign='>', value=0)

    if a >= 1e3:
        raise NumberValueError(num=a, sign='<', value=int(1e3))
    if b >= 1e3:
        raise NumberValueError(num=b, sign='<', value=int(1e3))
    
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
