import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), \
                             os.pardir))
from exceptions import IterableLengthError


def ini5(lines, save=False, path=None, filename='rosalind_ini5_1_output', ext='txt'):
    '''
    Returns a list containing all the even-numbered lines from the original list.

            Parameters:
                    lines (list): An input list of lines

                    save (bool): Boolean if you want to save result in a file
                    path (str): Path to either dir or file you want to save
                    filename (str): File name you want to save
                    ext (str): File extension you want to save

            Returns:
                    even_lines (list): List of even-numbered lines
    '''

    even_lines = []

    # assert len(lines) <= 1e3, f'Error: len(lines) = {len(lines)} must be <= 1000!'

    if len(lines) > 1e3:
        raise IterableLengthError(iterable=lines, sign='<=', value=int(1e3))

    for i in range(len(lines)):
        if i % 2 != 0:
            even_lines += [lines[i]]

    if save:
        if path is None:
            path = os.path.join(os.path.dirname(os.path.realpath(__file__)), \
                                f'{filename}.{ext}')
        elif os.path.isdir(path):
            path = os.path.join(path, f'{filename}.{ext}')
        with open(path,  'w') as file:
            file.writelines(even_lines)

    return even_lines


if __name__ == '__main__':
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), \
                           'rosalind_ini5_1_dataset.txt'), 'r') as file:
        lines = file.readlines()

    print(lines)  
    
    print(*ini5(lines, save=True))
