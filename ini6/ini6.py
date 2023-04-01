import os

class StringIsOutOfRange(Exception):
    def __init__(self, string, message=None):
        if message is None:
            message = 'Error: len(' + [name for name in globals() \
                                   if globals()[name] == string][0] \
                + ') = ' + str(len(string)) + ' must be less than 10000!'
        super().__init__(message)

path = os.path.join(os.getcwd(), \
                    os.path.basename(__file__).split('.')[0])

def ini6(s, save=False):
    result = {}
    
    words = s.split()
    for word in words:
        if word not in result.keys():
            result[word] = 1
        else:
            result[word] += 1

    if save:
        with open(os.path.join(path, 'rosalind_ini6_1_output.txt'), 'w') as file:
            for key, value in result.items():
                file.write(f'{key} {value}\n')

    return result

if __name__ == '__main__':
    with open(os.path.join(path, 'rosalind_ini6_1_dataset.txt'), 'r') as file:
        s = file.readline()

    # assert len(s) <= 1e4, f'Error: len(s) = {len(s)} must be less than 10000!'

    if len(s) > 1e4:
        raise StringIsOutOfRange(s)
    
    print(ini6(s, save=True))
