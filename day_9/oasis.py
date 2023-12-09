import click

def get_differences(history):
    all_differences = []

    # Compute first differences list from history
    differences = [history[idx+1] - history[idx] for idx in range(len(history)-1)]
    all_differences.append(differences)
            
    # Compute all other differences list until a list is all zeros
    while not all([ v == 0 for v in differences]):
        differences = [differences[idx+1] - differences[idx] for idx in range(len(differences)-1)]
        all_differences.append(differences)
    
    return all_differences


@click.command()
@click.option('--file', '-f', help='Input file name.')
def oasis1(file):
    """ Part 1 """
    res = []
    with open(file) as f:
        for line in f.read().splitlines():
            history = [int(val) for val in line.split(' ')]
            all_differences = get_differences(history)

            val_to_add = 0
            for idx, seq in enumerate(list(reversed(all_differences))):
                if idx == 0:
                    val_to_add = seq[-1]
                else:
                    val_to_add = seq[-1] + val_to_add
            next_val = history[-1] + val_to_add
            print(f'Next value is {next_val}')
            res.append(next_val)
    
    print(f'Result is {sum(res)}')

@click.command()
@click.option('--file', '-f', help='Input file name.')
def oasis2(file):
    """ Part 2 """
    res = []
    with open(file) as f:
        for line in f.read().splitlines():
            history = [int(val) for val in line.split(' ')]
            all_differences = get_differences(history)

            val_to_sub = 0
            for idx, seq in enumerate(list(reversed(all_differences))):
                if idx == 0:
                    val_to_sub = seq[0]
                else:
                    val_to_sub = seq[0] - val_to_sub
            prev_val = history[0] - val_to_sub
            print(f'Previous value is {prev_val}')
            res.append(prev_val)
    
    print(f'Result is {sum(res)}')

if __name__ == '__main__':
    oasis2()