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

def ini3(text, a, b, c, d, save=False):
    result = f'{text[a:b+1]} {text[c:d+1]}'

    if save:
        with open(os.path.join(path, 'rosalind_ini3_1_output.txt'), 'w') as file:
            file.write(result)

    return result

if __name__ == '__main__':
    with open(os.path.join(path, 'rosalind_ini3_1_dataset.txt'), 'r') as file:
        text = file.readline()
        a, b, c, d = list(map(int, file.readline().split()))

    print(text)
    print(a, b, c, d)

    # assert len(text) < 2e2, f'Error: len(text) = {len(text)} must be less than 200 letters!'

    if len(text) >= 2e2:
        raise StringIsOutOfRange(text)

    print(ini3(text, a, b, c, d, save=True))
