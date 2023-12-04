import click
import re

def get_list_of_digits(str_numbers):
    """ Get a list of digit out of a string """
    return [int(digit) for digit in re.findall(r'\d+', str_numbers)]

def parse_cards(file):
    res = [] # store the number of match of each card

    with open(file) as f:
        for line in f.readlines():
            # Create 2 lists (winning list & my list)
            subset_list = line.split(': ')[1][:-1].split(' | ')
            winning_list = get_list_of_digits(subset_list[0])
            my_list = get_list_of_digits(subset_list[1])

            # Check my list in winning
            match_number = set(my_list)&set(winning_list)
            res.append(len(match_number))

    return res


@click.command()
@click.option('--file', '-f', help='Input file name.')
def scratchcards(file):
    """ Part 1 """
    res_list = parse_cards(file)
    res = [2**(points - 1) if points != 0 else 0 for points in res_list]
    click.echo("Result is " + str(sum(res)))

@click.command()
@click.option('--file', '-f', help='Input file name.')
def scratchcards2(file):
    """ Part 2 """ 
    result = parse_cards(file)

    # store the number of instance of each card
    card_inst_list = []
    for card in range(0, len(result)):
        card_inst = 1 # always 1 at least
        for x in range(1, card + 1): # check all previous card result
            if result[card - x] >= x: # if result is bigger than diff
                card_inst += card_inst_list[card - x] # inc 
        card_inst_list.append(card_inst)
    
    click.echo("Result is " + str(sum(card_inst_list)))   


if __name__ == '__main__':
    scratchcards2()