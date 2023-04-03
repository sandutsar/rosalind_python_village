import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), \
                             os.pardir))
from exceptions import IterableLengthError

<<<<<<< Updated upstream

class _LinesOverflowError(Exception):
    def __init__(self, lines, message=None):
        if message is None:
            message = 'Error: len(' + [name for name in globals() \
                                            if globals()[name] == lines][0] \
                + ') = ' + str(len(lines)) + ' must be at most 1000!'
        super().__init__(message)
=======
>>>>>>> Stashed changes


def ini5(lines, path=None, save=False):
    result = []

    # assert len(lines) <= 1e3, f'Error: len(lines) = {len(lines)} must be <= 1000!'

    if len(lines) > 1e3:
<<<<<<< Updated upstream
        raise _LinesOverflowError(lines)
=======
        raise IterableLengthError(iterable=lines, sign='<=', value=int(1e3))
>>>>>>> Stashed changes

    for i in range(len(lines)):
        if i % 2 != 0:
            result += [lines[i]]

    if save:
        if path is None:
            path = os.path.join(os.path.dirname(os.path.realpath(__file__)), \
                                'rosalind_ini5_1_output.txt')
        else:
            path = os.path.join(path, 'rosalind_ini5_1_output.txt')
        with open(path,  'w') as file:
            file.writelines(result)

    return result


if __name__ == '__main__':
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), \
                           'rosalind_ini5_1_dataset.txt'), 'r') as file:
        lines = file.readlines()

    print(lines)  
    
    print(*ini5(lines, save=True))
