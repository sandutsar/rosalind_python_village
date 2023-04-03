import os


class _StringOverflowError(Exception):
    def __init__(self, string, message=None):
        if message is None:
            message = 'Error: len(' + [name for name in globals() \
                                   if globals()[name] == string][0] \
                + ') = ' + str(len(string)) + ' must be at most 200!'
        super().__init__(message)


def ini3(s, a, b, c, d, path=None, save=False):
    # assert len(s) <= 2e2, f'Error: len(s) = {len(s)} must be at most 200!'

    if len(s) > 2e2:
        raise _StringOverflowError(s)
    
    result = (s[a:b+1], s[c:d+1])

    if save:
        if path is None:
            path = os.path.join(os.path.dirname(os.path.realpath(__file__)), \
                                'rosalind_ini3_1_output.txt')
        else:
            path = os.path.join(path, 'rosalind_ini3_1_output.txt')
        with open(path, 'w') as file:
            file.write(' '.join(result))

    return result


if __name__ == '__main__':
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), \
                           'rosalind_ini3_1_dataset.txt'), 'r') as file:
        s = file.readline()
        a, b, c, d = list(map(int, file.readline().split()))

    print(s)
    print(a, b, c, d)

    print(*ini3(s, a, b, c, d, save=True))
