import click
import re

@click.command()
@click.option('--file', '-f', help='Input file name.')
def engine(file):
    """ Part 1 """
    index_list = dict()
    number_list = []
    last_index = 0

    # First loop to get special character and their index
    with open(file) as f:
        for idx, line in enumerate(f.readlines()):
            line_idx_list = []
            for item in re.finditer(r'[\*\#\+\-\=\$\\\/\@\&\%]', line):
                line_idx_list.append(item.start())
            index_list[idx] = line_idx_list
            last_index = idx

    # Second loop to get the numbers...
    with open(file) as f:
        for idx, line in enumerate(f.readlines()):
            for number in re.finditer(r'\d+', line):    
                if index_list[idx]:
                    for i in index_list[idx]:
                        if number.start() == i+1 or number.end() == i:
                            number_list.append(int(number.group()))
                if idx != 0 and index_list[idx-1]:
                    for i in index_list[idx-1]:
                        if number.start() == i-1 or number.start() == i or number.start() == i+1 or number.end() == i or number.end() == i+1:
                            number_list.append(int(number.group()))
                if idx != last_index and index_list[idx+1]:
                    for i in index_list[idx+1]:
                        if number.start() == i-1 or number.start() == i or number.start() == i+1 or number.end() == i or number.end() == i+1:
                            number_list.append(int(number.group()))

    click.echo("Result is " + str(sum(number_list)))

if __name__ == '__main__':
    engine()