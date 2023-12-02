import click

def decode_game(game):
    """
    Returns a dictonary with the number of cubes for each valid color
    """
    valid_colors = ['red', 'green', 'blue']

    # Get a list of all subsets of a game
    # 'Game X: ' and last '\n' are removed, the rest is sliced each ';'
    subset_list = game.split(': ')[1][:-1].split('; ')
    subset_dict = dict()

    for subset in subset_list:
        # ',' are removed and the rest is sliced each ' '
        subset = subset.replace(',', '').split(' ')
        for color in valid_colors:
            for idx, s in enumerate(subset):
                if s == color:
                    if subset_dict.get(color) is None or int(subset_dict.get(color)) < int(subset[idx-1]) :
                        subset_dict[color] = subset[idx-1]
    # print(subset_dict)
    return subset_dict

@click.command()
@click.option('--file', '-f', help='Input file name.')
@click.option('--red', '-r', help='Number of red cubes.')
@click.option('--green', '-g', help='Number of green cubes.')
@click.option('--blue', '-b', help='Number of blue cubes.')
def cube(file, red, green, blue):
    """ Part 1 """
    with open(file) as f:
        game = 1
        possible = []
        for line in f.readlines():
            subset_dict = decode_game(line)

            # Check if the game is possible compared to the input
            if int(subset_dict['red']) <= int(red) and int(subset_dict['green']) <= int(green) and int(subset_dict['blue']) <= int(blue):
                possible.append(game)

            # Increment game ID (suppose that games are ordered...)
            game += 1

        print('Following game ID are possible: ', possible)
        print('Sum is: ', sum(possible))

@click.command()
@click.option('--file', '-f', help='Input file name.')
def cube_power(file):
    """ Part 2 """
    with open(file) as f:
        power = []
        for line in f.readlines():
            subset_dict = decode_game(line)
            power.append(int(subset_dict['red']) * int(subset_dict['green']) * int(subset_dict['blue']))

        print('Sum is: ', sum(power))

if __name__ == '__main__':
    cube_power()