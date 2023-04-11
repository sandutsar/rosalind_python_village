import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), \
                             os.pardir))
from exceptions import IterableLengthError


def ini3(s, a, b, c, d, path=None, save=False):
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
    
    result = (s[a:b+1], s[c:d+1])

    if save:
        if path is None:
            path = os.path.join(os.path.dirname(os.path.realpath(__file__)), \
                                'rosalind_ini3_1_output.txt')
        elif os.path.isdir(path):
            path = os.path.join(path, 'rosalind_ini3_1_output.txt')
        with open(path, 'w') as file:
            file.write(' '.join(result))

    return result


if __name__ == '__main__':
    if len(sys.argv) == 6:
        s = sys.argv[1]
        a, b, c, d = [int(x) for x in sys.argv[2:]]
    else:
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), \
                            'rosalind_ini3_1_dataset.txt'), 'r') as file:
            s = file.readline()
            a, b, c, d = list(map(int, file.readline().split()))

    print(s)
    print(a, b, c, d)

    print(*ini3(s, a, b, c, d, save=True))
