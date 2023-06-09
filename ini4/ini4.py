import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), \
                             os.pardir))
from exceptions import NumberValueError

def ini4(a, b, save=False, path=None, filename='rosalind_ini4_1_output', ext='txt'):
    '''
    Returns the sum of all odd integers from a through b, inclusively.

            Parameters:
                    a (int): Low limit of integers range
                    b (int): High limit of integers range

                    save (bool): Boolean if you want to save result in a file
                    path (str): Path to either dir or file you want to save
                    filename (str): File name you want to save
                    ext (str): File extension you want to save

            Returns:
                    odd_sum (int): Odd integers sum
    '''

    odd_sum = 0

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
        # raise ValueError(f'Error: a = {a} must be > 0!')
        raise NumberValueError(num=a, sign='>', value=0)
    if b <= 0:
        # raise ValueError(f'Error: b = {b} must be > 0!')
        raise NumberValueError(num=b, sign='>', value=0)
    
    if a >= 1e4:
        # raise OverflowError(f'Error: a = {a} must be < 10000!')
        raise NumberValueError(num=a, sign='<', value=int(1e4))
    if b >= 1e4:
        # raise OverflowError(f'Error: b = {b} must be < 10000!')
        raise NumberValueError(num=b, sign='<', value=int(1e4))
    
    assert a < b, f'Error: a = {a} must be < b = {b}!'

    odd_sum = sum([num if num % 2 != 0 else 0 for num in range(a, b + 1)])

    if save:
        if path is None:
            path = os.path.join(os.path.dirname(os.path.realpath(__file__)), \
                                f'{filename}.{ext}')
        elif os.path.isdir(path):
            path = os.path.join(path, f'{filename}.{ext}')
        with open(path, 'w') as file:
            file.write(str(odd_sum))

    return odd_sum


if __name__ == '__main__':
    if len(sys.argv) == 3:
        try:
            a, b = list(map(int, sys.argv[1:]))
        except ValueError as e:
            print(f'Error: {e}!')
            sys.exit(f'Usage: {sys.argv[0]} <a(int)> <b(int)>')
    else:
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), \
                            'rosalind_ini4_1_dataset.txt'), 'r') as file:
            a, b = list(map(int, file.readline().split()))

    print(a, b)
    
    # print(help(ini1))
    # print(ini1.__doc__)
    print(ini4(a, b, save=True))
