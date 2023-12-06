import click
import re
from operator import mul
from functools import reduce

@click.command()
@click.option('--file', '-f', help='Input file name.')
def boat_race1(file):
    """ Part 1 """
    with open(file) as f:
        subset = f.read().split(':')
        time = [int(num) for num in re.findall(r'\d+', subset[1])]
        dist = [int(num) for num in re.findall(r'\d+', subset[2])]
        print(f'Time {time} and distance {dist}')

    way_to_win_list = []
    for t_idx, t in enumerate(time):
        way_to_win = 0
        for i in range(1, t):
            i_dist = (t - i)*i
            if i_dist > dist[t_idx]:
                way_to_win += 1
        way_to_win_list.append(way_to_win)
        print(f'Time {t} has {way_to_win} ways to win')
    print(f'Result is {reduce(mul, way_to_win_list)}')


@click.command()
@click.option('--file', '-f', help='Input file name.')
def boat_race2(file):
    """ Part 1 """
    with open(file) as f:
        subset = f.read().split(':')
        time = [int(num) for num in re.findall(r'\d+', subset[1].replace(' ', ''))][0]
        dist = [int(num) for num in re.findall(r'\d+', subset[2].replace(' ', ''))][0]
        print(f'Time {time} and distance {dist}')
    
    way_to_win = 0
    for i in range(1, time):
        i_dist = (time - i)*i
        if i_dist > dist:
            way_to_win += 1
    print(f'Result is {way_to_win} ways to win')        

if __name__ == '__main__':
    boat_race2()