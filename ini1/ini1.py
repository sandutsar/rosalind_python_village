import os, this


def ini1(save=False, path=None, filename='rosalind_ini1_1_output', ext='txt'):
    '''
    Returns `The Zen of Python` as string.

            Parameters:
                    save (bool): Boolean if you want to save result in a file
                    path (str): Path to either dir or file you want to save
                    filename (str): File name you want to save
                    ext (str): File extension you want to save

            Returns:
                    zen (str): String containig `The Zen of Python`
    '''

    zen = "".join([this.d.get(c, c) for c in this.s][34:])

    if save:
        if path is None:
            path = os.path.join(os.path.dirname(os.path.realpath(__file__)), \
                                f'{filename}.{ext}')
        elif os.path.isdir(path):
            path = os.path.join(path, f'{filename}.{ext}')
        with open(path, 'w') as file:
            file.write(zen)

    return zen


if __name__ == '__main__':
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), \
                           'rosalind_ini1_1_dataset.txt'), 'r') as file:
        print(f'\n{file.readline()}')

    # print(help(ini1))
    # print(ini1.__doc__)
    print(ini1(save=True))
