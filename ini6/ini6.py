import os

class _StringIsOutOfRange(Exception):
    def __init__(self, string, message=None):
        if message is None:
            message = 'Error: len(' + [name for name in globals() \
                                   if globals()[name] == string][0] \
                + ') = ' + str(len(string)) + ' must be at most 10000!'
        super().__init__(message)

def ini6(s, path=None, save=False):
    result = {}

    # assert len(s) <= 1e4, f'Error: len(s) = {len(s)} must be at most 10000!'

    if len(s) > 1e4:
        raise _StringIsOutOfRange(s)
    
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
        else:
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
