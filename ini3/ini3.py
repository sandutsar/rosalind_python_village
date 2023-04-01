import os

class StringIsOutOfRange(Exception):
    def __init__(self, string, message=None):
        if message is None:
            message = 'Error: len(' + [name for name in globals() \
                                   if globals()[name] == string][0] \
                + ') = ' + str(len(string)) + ' must be less than 200!'
        super().__init__(message)

path = os.path.join(os.getcwd(), \
                    os.path.basename(__file__).split('.')[0])

def ini3(s, a, b, c, d, save=False):
    result = f'{s[a:b+1]} {s[c:d+1]}'

    if save:
        with open(os.path.join(path, 'rosalind_ini3_1_output.txt'), 'w') as file:
            file.write(result)

    return result

if __name__ == '__main__':
    with open(os.path.join(path, 'rosalind_ini3_1_dataset.txt'), 'r') as file:
        s = file.readline()
        a, b, c, d = list(map(int, file.readline().split()))

    print(s)
    print(a, b, c, d)

    # assert len(s) < 2e2, f'Error: len(s) = {len(s)} must be less than 200 letters!'

    if len(s) >= 2e2:
        raise StringIsOutOfRange(s)

    print(ini3(s, a, b, c, d, save=True))
