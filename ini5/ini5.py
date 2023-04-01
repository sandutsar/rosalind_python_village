import os

class LinesIsOutOfRange(Exception):
    def __init__(self, lines, message=None):
        if message is None:
            message = 'Error: len(' + [name for name in globals() \
                                            if globals()[name] == lines][0] \
                + ') = ' + str(len(lines)) + ' must be less than 1000!'
        super().__init__(message)

path = os.path.join(os.getcwd(), \
                    os.path.basename(__file__).split('.')[0])

def ini5(lines, save=False):
    result = []

    for i in range(len(lines)):
        if i % 2 != 0:
            result += [lines[i]]

    if save:
        with open(os.path.join(path, 'rosalind_ini5_1_output.txt'), 'w') as file:
            file.writelines(result)

    return result

if __name__ == '__main__':
    with open(os.path.join(path, 'rosalind_ini5_1_dataset.txt'), 'r') as file:
        lines = file.readlines()

    print(lines)
   
    # assert len(lines) < 1e3, f'Error: len(lines) = {len(lines)} must be less than 1000!'

    if len(lines) > 1e3:
        raise LinesIsOutOfRange(lines)
    
    print(*ini5(lines, save=True))
