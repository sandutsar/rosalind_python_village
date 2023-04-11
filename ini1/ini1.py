import os, this


def ini1(save=False, path=None, filename='rosalind_ini1_1_output', ext='txt'):
    result = "".join([this.d.get(c, c) for c in this.s][34:])

    if save:
        if path is None:
            path = os.path.join(os.path.dirname(os.path.realpath(__file__)), \
                                f'{filename}.{ext}')
        elif os.path.isdir(path):
            path = os.path.join(path, f'{filename}.{ext}')
        with open(path, 'w') as file:
            file.write(result)

    return result


if __name__ == '__main__':
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), \
                           'rosalind_ini1_1_dataset.txt'), 'r') as file:
        print(f'\n{file.readline()}')

    print(ini1(save=True))
