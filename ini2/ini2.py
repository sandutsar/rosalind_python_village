import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), \
                             os.pardir))
from exceptions import NumberValueError


def ini2(a, b, save=False, path=None, filename='rosalind_ini2_1_output', ext='txt'):
    '''
    Returns the integer corresponding to the square of the hypotenuse of the right triangle whose legs have lengths a and b.

            Parameters:
                    a (int): A leg of the right triangle
                    b (int): Another leg of the right triangle

                    save (bool): Boolean if you want to save result in a file
                    path (str): Path to either dir or file you want to save
                    filename (str): File name you want to save
                    ext (str): File extension you want to save

            Returns:
                    hypotenuse_squared (int): The square of the hypotenuse
    '''

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
        # raise ValueError(f'Error: a = {a} must be > 0!')
        raise NumberValueError(num=a, sign='>', value=0)
    if b <= 0:
        # raise ValueError(f'Error: b = {b} must be > 0!')
        raise NumberValueError(num=b, sign='>', value=0)

    if a >= 1e3:
        # raise OverflowError(f'Error: a = {a} must be < 1000!')
        raise NumberValueError(num=a, sign='<', value=int(1e3))
    if b >= 1e3:
        # raise OverflowError(f'Error: b = {b} must be < 1000!')
        raise NumberValueError(num=b, sign='<', value=int(1e3))
    
    hypotenuse_squared = a*a + b*b

    if save:
        if path is None:
            path = os.path.join(os.path.dirname(os.path.realpath(__file__)), \
                                f'{filename}.{ext}')
        elif os.path.isdir(path):
            path = os.path.join(path, f'{filename}.{ext}')
        with open(path, 'w') as file:
            file.write(str(hypotenuse_squared))

    return hypotenuse_squared


if __name__ == '__main__':
    if len(sys.argv) == 3:
        try:
            a, b = list(map(int, sys.argv[1:]))
        except ValueError as e:
            print(f'Error: {e}!')
            sys.exit(f'Usage: {sys.argv[0]} <a(int)> <b(int)>')
    else:
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), \
                            'rosalind_ini2_1_dataset.txt'), 'r') as file:
            a, b = list(map(int, file.readline().split()))

    print(a, b)
    
    # print(help(ini2))
    # print(ini2.__doc__)
    print(ini2(a, b, save=True))
