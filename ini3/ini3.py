import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), \
                             os.pardir))
from exceptions import IterableLengthError


def ini3(s, a, b, c, d, save=False, path=None, filename='rosalind_ini3_1_output', ext='txt'):
    '''
    Returns tuple of 2 slices of a string from indices a through b and c through d (with space in between), inclusively.

            Parameters:
                    s (str): An input string
                    a (int): An integer representing string index
                    b (int): An integer representing string index
                    c (int): An integer representing string index
                    d (int): An integer representing string index

                    save (bool): Boolean if you want to save result in a file
                    path (str): Path to either dir or file you want to save
                    filename (str): File name you want to save
                    ext (str): File extension you want to save

            Returns:
                    string_slice (tuple): Tuple containig 2 string slices
    '''

    # assert isinstance(s, str), f'Error: type(s) = {type(s).__name__} must be str!'
    # assert len(s) <= 2e2, f'Error: len(s) = {len(s)} must be <= 200!'

    # assert isinstance(a, int), f'Error: type(a) = {type(a).__name__} must be int!'
    # assert isinstance(b, int), f'Error: type(b) = {type(b).__name__} must be int!'
    # assert isinstance(c, int), f'Error: type(c) = {type(c).__name__} must be int!'
    # assert isinstance(d, int), f'Error: type(d) = {type(d).__name__} must be int!'

    if not isinstance(s, str):
        raise TypeError(f'Error: type(s) = {type(s).__name__} must be str!')
    if len(s) > 2e2:
        raise IterableLengthError(iterable=s, sign='<=', value=int(2e2))
    
    if not isinstance(a, int):
        raise TypeError(f'Error: type(a) = {type(a).__name__} must be int!')
    if not isinstance(b, int):
        raise TypeError(f'Error: type(b) = {type(b).__name__} must be int!')
    if not isinstance(c, int):
        raise TypeError(f'Error: type(c) = {type(c).__name__} must be int!')
    if not isinstance(d, int):
        raise TypeError(f'Error: type(d) = {type(d).__name__} must be int!')
    
    if a > b:
        raise ValueError(f'Error: a = {a} must be < b = {b}')
    if c > d:
        raise ValueError(f'Error: c = {c} must be < d = {d}')
    
    string_slice = (s[a:b+1], s[c:d+1])

    if save:
        if path is None:
            path = os.path.join(os.path.dirname(os.path.realpath(__file__)), \
                                f'{filename}.{ext}')
        elif os.path.isdir(path):
            path = os.path.join(path, f'{filename}.{ext}')
        with open(path, 'w') as file:
            file.write(' '.join(string_slice))

    return string_slice


if __name__ == '__main__':
    if len(sys.argv) == 6:
        try:
            s = sys.argv[1]
            a, b, c, d = list(map(int, sys.argv[2:]))
        except ValueError as e:
            print(f'Error: {e}!')
            sys.exit(f'Usage: {sys.argv[0]} <s(str)> <a(int)> <b(int)> <c(int)> <d(int)>')
    else:
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), \
                            'rosalind_ini3_1_dataset.txt'), 'r') as file:
            s = file.readline()
            a, b, c, d = list(map(int, file.readline().split()))

    print(s)
    print(a, b, c, d)

    # print(help(ini3))
    # print(ini3.__doc__)
    print(*ini3(s, a, b, c, d, save=True))
