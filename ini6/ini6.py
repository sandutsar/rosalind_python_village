import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), \
                             os.pardir))
from exceptions import IterableLengthError


def ini6(s, save=False, path=None, filename='rosalind_ini6_1_output', ext='txt'):
    '''
    Returns dictionary with the number of occurrences of each word in s.

            Parameters:
                    s (str): An input string

                    save (bool): Boolean if you want to save result in a file
                    path (str): Path to either dir or file you want to save
                    filename (str): File name you want to save
                    ext (str): File extension you want to save

            Returns:
                    words_dict (dict): Dictionary of all word occurrences in s
    '''
    
    words_dict = {}

    # assert isinstance(s, str), f'Error: type(s) = {type(s).__name__} must be str!'
    # assert len(s) <= 1e4, f'Error: len(s) = {len(s)} must be <= 10000!'

    if not isinstance(s, str):
        raise TypeError(f'Error: type(s) = {type(s).__name__} must be str!')
    if len(s) > 1e4:
        raise IterableLengthError(iterable=s, sign='<=', value=int(1e4))
    
    words = s.split()
    for word in words:
        if word not in words_dict.keys():
            words_dict[word] = 1
        else:
            words_dict[word] += 1

    if save:
        if path is None:
            path = os.path.join(os.path.dirname(os.path.realpath(__file__)), \
                                f'{filename}.{ext}')
        elif os.path.isdir(path):
            path = os.path.join(path, f'{filename}.{ext}')
        with open(path,  'w') as file:
            for key, value in words_dict.items():
                file.write(f'{key} {value}\n')

    return words_dict


if __name__ == '__main__':
    if len(sys.argv) == 2:
        s = sys.argv[1]
    else:
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), \
                            'rosalind_ini6_1_dataset.txt'), 'r') as file:
            s = file.readline()

    print(s)
    
    print(ini6(s, save=True))
