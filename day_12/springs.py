import click
from collections import Counter
from itertools import product

def is_valid(state, spring):
    reorg_state = [s for s in state.split('.') if s != '']
    if len(reorg_state) == len(spring):
        return all([ len(s) == spring[i] for i, s in enumerate(reorg_state)])
    else:
        return False

@click.command()
@click.option('--file', '-f', help='Input file name.')
def springs1(file):
    """ Part 1 """
    res = []
    with open(file) as f:
        for line in f.read().splitlines():
            springs = line.split(' ')[1].split(',')
            springs = [int(s) for s in springs]
            states = list(line.split(' ')[0])
            
            options = ['#', '.']
            N = Counter(states)['?'] # numbers of '?'
            possibilities = [list(t) for t in (product(*(options,)*N))] # list of possible permutations
        
            counter = 0
            for possibility in possibilities:
                test = []
                i = 0
                for s in states:
                    if s == '?':
                        test.append(possibility[i])
                        i += 1
                    else:
                        test.append(s)
                if is_valid(''.join(test), springs):
                    counter += 1
            res.append(counter)
            print(f'Number of possibilities is {counter}')
            
    print(f'Result is {sum(res)}')
            

if __name__ == '__main__':
    springs1()