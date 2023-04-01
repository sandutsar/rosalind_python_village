import os, this

path = os.path.join(os.getcwd(), \
                    os.path.basename(__file__).split('.')[0])

def ini1(save=False):
    result = "".join([this.d.get(c, c) for c in this.s][34:])

    if save:
        with open(os.path.join(path, 'rosalind_ini1_1_output.txt'), 'w') as file:
            file.write(result)

    return result

if __name__ == '__main__':
    with open(os.path.join(path, 'rosalind_ini1_1_dataset.txt'), 'r') as file:
        print(f'\n{file.readline()}')

    print(ini1(save=True))
