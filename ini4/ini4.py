import os

class NumberIsOutOfRange(Exception):
    def __init__(self, num, message=None):
        if message is None:
            message = 'Error: ' + [name for name in globals() \
                                   if globals()[name] == num][0] \
                + ' = ' + str(num) + ' must be less than 10000!'
        super().__init__(message)

path = os.path.join(os.getcwd(), \
                    os.path.basename(__file__).split('.')[0])

def ini4(a, b, save=False):
    result = 0

    for num in range(a, b + 1):
        if num % 2 != 0:
            result += num

    if save:
        with open(os.path.join(path, 'rosalind_ini4_1_output.txt'), 'w') as file:
            file.write(str(result))

    return result

if __name__ == '__main__':
    with open(os.path.join(path, 'rosalind_ini4_1_dataset.txt'), 'r') as file:
        a, b = list(map(int, file.readline().split()))

    print(a, b)
    
    # assert a < 1e4, f'Error: a = {a} must be less than 10000!'
    # assert b < 1e4, f'Error: b = {b} must be less than 10000!'
    
    if a >= 1e4:
        raise NumberIsOutOfRange(a)
    if b >= 1e4:
        raise NumberIsOutOfRange(b)
    
    print(ini4(a, b, save=True))
