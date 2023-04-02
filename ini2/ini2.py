import os

class _NumberIsOutOfRange(Exception):
    def __init__(self, num, message=None):
        if message is None:
            message = 'Error: ' + [name for name in globals() \
                                   if globals()[name] == num][0] \
                + ' = ' + str(num) + ' must be less than 1000!'
        super().__init__(message)

def ini2(a, b, path=None, save=False):
    result = a*a + b*b

    # assert a < 1e3, f'Error: a = {a} must be less than 1000!'
    # assert b < 1e3, f'Error: b = {b} must be less than 1000!'
    
    if a >= 1e3:
        raise _NumberIsOutOfRange(a)
    if b >= 1e3:
        raise _NumberIsOutOfRange(b)

    if save:
        if path is None:
            path = os.path.join(os.getcwd(), os.path.basename(__file__).split('.')[0], \
                                'rosalind_ini2_1_output.txt')
        else:
            path = os.path.join(path, 'rosalind_ini2_1_output.txt')
        with open(path, 'w') as file:
            file.write(str(result))

    return result

if __name__ == '__main__':
    with open(os.path.join(os.getcwd(), os.path.basename(__file__).split('.')[0], \
                           'rosalind_ini2_1_dataset.txt'), 'r') as file:
        a, b = list(map(int, file.readline().split()))

    print(a, b)
  
    print(ini2(a, b, save=True))
