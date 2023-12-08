import click
import re
import math

def parsing(file):
    """ 
    Parse input file
    Returns a list of instructions and a dict of node names with their 
    left and right nodes 
    """
    all_nodes = dict()
    with open(file) as f:
        for idx, line in enumerate(f.read().splitlines()):
            if idx == 0:
                instructions = list(line)
            elif idx > 1:
                node = [x for x in re.findall('[1-9A-Z]+', line)]
                all_nodes[node[0]] = {'L': node[1], 'R': node[2]}
    return instructions, all_nodes

@click.command()
@click.option('--file', '-f', help='Input file name.')
def wasteland1(file):
    """ Part 1 """

    # File parsing 
    instructions, all_nodes = parsing(file)

    current_node = 'AAA' # First node
    steps = 0 # Steps counter
    while current_node != 'ZZZ':
        current_node = all_nodes[current_node][instructions[steps % len(instructions)]]
        steps += 1
                
    print(f'Result is {steps}')

@click.command()
@click.option('--file', '-f', help='Input file name.')
def wasteland2(file):
    """ Part 2 """

    # File parsing 
    instructions, all_nodes = parsing(file)
    
    possible_nodes = [node for node in all_nodes.keys() if node[2] == 'A'] # First nodes list
    steps = [0] * len(possible_nodes) # Steps counter
    
    for idx, node in enumerate(possible_nodes):
        while node[2] != 'Z':
            node = all_nodes[node][instructions[steps[idx] % len(instructions)]]
            steps[idx] += 1

    print(f'Result is {math.lcm(*steps)}')  # lcm() needs python3.9

if __name__ == '__main__':
    wasteland2()