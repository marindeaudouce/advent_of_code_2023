import click
import re

def correspondance(x, x_y_map):
    for i in x_y_map:
        if i[1] <= x and x <= (i[1] + i[2] - 1):
            y = i[0] + (x - i[1])
    if 'y' not in locals():
        y = x
    return y

def get_map(subset):
    my_map = [int(num) for num in re.findall(r'\d+', subset)]
    return [my_map[i:i+3] for i in range(0,len(my_map),3)]

@click.command()
@click.option('--file', '-f', help='Input file name.')
def almanac1(file):
    """ Part 1 """
    with open(file) as f:
        subset = f.read().split(':')

        seeds = [int(num) for num in re.findall(r'\d+', subset[1])]
        seed_soil_map = get_map(subset[2])
        soil_fert_map = get_map(subset[3])
        fert_water_map = get_map(subset[4])
        water_light_map = get_map(subset[5])
        light_temp_map = get_map(subset[6])
        temp_hum_map = get_map(subset[7])
        hum_loc_map = get_map(subset[8])
        
    print(f'Seeds are {seeds}')
    # Map known seed numbers
    loc_list = []
    for seed in seeds:
        soil = correspondance(seed, seed_soil_map)
        fert = correspondance(soil, soil_fert_map)
        water = correspondance(fert, fert_water_map)
        light = correspondance(water, water_light_map)
        temp = correspondance(light, light_temp_map)
        hum = correspondance(temp, temp_hum_map)
        loc = correspondance(hum, hum_loc_map)     
        loc_list.append(loc)
        print(f'{seed} to {soil} to {fert} to {water} to {light} to {temp} to {hum} to {loc}')

    print(f'Lowest location is {min(loc_list)}')

if __name__ == '__main__':
    almanac1()