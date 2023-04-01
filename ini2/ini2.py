import os

class NumberIsOutOfRange(Exception):
    def __init__(self, num, message=None):
        if message is None:
            message = 'Error: ' + [name for name in globals() \
                                   if globals()[name] == num][0] \
                + ' = ' + str(num) + ' must be less than 1000!'
        super().__init__(message)

path = os.path.join(os.getcwd(), \
                    os.path.basename(__file__).split('.')[0])

def ini2(a, b, save=False):
    result = a*a + b*b

    if save:
        with open(os.path.join(path, 'rosalind_ini2_1_output.txt'), 'w') as file:
            file.write(str(result))

    return result

if __name__ == '__main__':
    with open(os.path.join(path, 'rosalind_ini2_1_dataset.txt'), 'r') as file:
        a, b = list(map(int, file.readline().split()))

    print(a, b)
  
    # assert a < 1e3, f'Error: a = {a} must be less than 1000!'
    # assert b < 1e3, f'Error: b = {b} must be less than 1000!'
    
    if a >= 1e3:
        raise NumberIsOutOfRange(a)
    if b >= 1e3:
        raise NumberIsOutOfRange(b)

    print(ini2(a, b, save=True))
