import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), \
                             os.pardir))
from exceptions import IterableLengthError


def ini6(s, path=None, save=False):
    result = {}

    # assert isinstance(s, str), f'Error: type(s) = {type(s).__name__} must be str!'
    # assert len(s) <= 1e4, f'Error: len(s) = {len(s)} must be <= 10000!'

    if not isinstance(s, str):
        raise TypeError(f'Error: type(s) = {type(s).__name__} must be str!')
    if len(s) > 1e4:
        raise IterableLengthError(iterable=s, sign='<=', value=int(1e4))
    
    words = s.split()
    for word in words:
        if word not in result.keys():
            result[word] = 1
        else:
            result[word] += 1

    if save:
        if path is None:
            path = os.path.join(os.path.dirname(os.path.realpath(__file__)), \
                                'rosalind_ini6_1_output.txt')
        elif os.path.isdir(path):
            path = os.path.join(path, 'rosalind_ini6_1_output.txt')
        with open(path,  'w') as file:
            for key, value in result.items():
                file.write(f'{key} {value}\n')

    return result


if __name__ == '__main__':
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), \
                           'rosalind_ini6_1_dataset.txt'), 'r') as file:
        s = file.readline()

    print(s)
    
    print(ini6(s, save=True))
