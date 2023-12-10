import click

def check_top(coord1, coord2):
    """ Return True if [x2, y2] is at the top of [x1, y1] """
    if coord2[1] == coord1[1] and coord2[0] == coord1[0] - 1:
        return True
    else:
        return False

def check_bottom(coord1, coord2):
    """ Return True if [x2, y2] is at the bottom of [x1, y1] """
    if coord2[1] == coord1[1] and coord2[0] == coord1[0] + 1:
        return True
    else:
        return False

def check_left(coord1, coord2):
    """ Return True if [x2, y2] is on the left of [x1, y1] """
    if coord2[0] == coord1[0] and coord2[1] == coord1[1] - 1:
        return True
    else:
        return False

def check_right(coord1, coord2):
    """ Return True if [x2, y2] is on the right of [x1, y1] """
    if coord2[0] == coord1[0] and coord2[1] == coord1[1] + 1:
        return True
    else:
        return False

def compute_next_S(tiles, coordinate):
    two_tiles = []
    for t in tiles:
        if (t['tile'] == '-' and (check_left(coordinate, t['coordinate']) or \
        check_right(coordinate, t['coordinate']))):
            two_tiles.append({'tile': t['tile'], 'coordinate': t['coordinate']})
        elif (t['tile'] == '|' and (check_top(coordinate, t['coordinate']) or \
        check_bottom(coordinate, t['coordinate']))):
            two_tiles.append({'tile': t['tile'], 'coordinate':t['coordinate']})
        elif (t['tile'] == 'L' and (check_left(coordinate, t['coordinate']) or \
        check_bottom(coordinate, t['coordinate']))):
            two_tiles.append({'tile': t['tile'], 'coordinate': t['coordinate']})
        elif (t['tile'] == 'J' and (check_right(coordinate, t['coordinate']) or \
        check_bottom(coordinate, t['coordinate']))):
            two_tiles.append({'tile': t['tile'], 'coordinate': t['coordinate']})
        elif (t['tile'] == '7' and (check_right(coordinate, t['coordinate']) or \
        check_top(coordinate, t['coordinate']))):
            two_tiles.append({'tile': t['tile'], 'coordinate': t['coordinate']})
        elif (t['tile'] == 'F' and (check_left(coordinate, t['coordinate']) or \
        check_top(coordinate, t['coordinate']))):
            two_tiles.append({'tile': t['tile'], 'coordinate': t['coordinate']})
        
    return two_tiles

def compute_next_v(tiles, coordinate):
    two_tiles = []
    for t in tiles:
        if(t['tile'] == 'S' and (check_top(coordinate, t['coordinate']) or \
        check_bottom(coordinate, t['coordinate']))):
            two_tiles.append({'tile': t['tile'], 'coordinate': t['coordinate']})
        elif (t['tile'] == '|' and (check_top(coordinate, t['coordinate']) or \
        check_bottom(coordinate, t['coordinate']))):
            two_tiles.append({'tile': t['tile'], 'coordinate': t['coordinate']})
        elif (t['tile'] == 'L' and check_bottom(coordinate, t['coordinate'])):
            two_tiles.append({'tile': t['tile'], 'coordinate': t['coordinate']})
        elif (t['tile'] == 'J' and check_bottom(coordinate, t['coordinate'])):
            two_tiles.append({'tile': t['tile'], 'coordinate': t['coordinate']})
        elif (t['tile'] == '7' and check_top(coordinate, t['coordinate'])):
            two_tiles.append({'tile': t['tile'], 'coordinate': t['coordinate']})
        elif (t['tile'] == 'F' and check_top(coordinate, t['coordinate'])):
            two_tiles.append({'tile': t['tile'], 'coordinate': t['coordinate']})
        
    return two_tiles

def compute_next_h(tiles, coordinate):
    two_tiles = []
    for t in tiles:
        if(t['tile'] == 'S' and (check_left(coordinate, t['coordinate']) or \
        check_right(coordinate, t['coordinate']))):
            two_tiles.append({'tile': t['tile'], 'coordinate': t['coordinate']})
        elif (t['tile'] == '-' and (check_left(coordinate, t['coordinate']) or \
        check_right(coordinate, t['coordinate']))):
            two_tiles.append({'tile': t['tile'], 'coordinate': t['coordinate']})
        elif (t['tile'] == 'L' and check_left(coordinate, t['coordinate'])):
            two_tiles.append({'tile': t['tile'], 'coordinate': t['coordinate']})
        elif (t['tile'] == 'J' and check_right(coordinate, t['coordinate'])):
            two_tiles.append({'tile': t['tile'], 'coordinate': t['coordinate']})
        elif (t['tile'] == '7' and check_right(coordinate, t['coordinate'])):
            two_tiles.append({'tile': t['tile'], 'coordinate': t['coordinate']})
        elif (t['tile'] == 'F' and check_left(coordinate, t['coordinate'])):
            two_tiles.append({'tile': t['tile'], 'coordinate': t['coordinate']})
        
    return two_tiles

def compute_next_L(tiles, coordinate):
    two_tiles = []
    for t in tiles:
        if(t['tile'] == 'S' and (check_right(coordinate, t['coordinate']) or \
        check_top(coordinate, t['coordinate']))):
            two_tiles.append({'tile': t['tile'], 'coordinate': t['coordinate']})
        elif (t['tile'] == '-' and check_right(coordinate, t['coordinate'])):
            two_tiles.append({'tile': t['tile'], 'coordinate': t['coordinate']})
        elif (t['tile'] == '|' and check_top(coordinate, t['coordinate'])):
            two_tiles.append({'tile': t['tile'], 'coordinate': t['coordinate']})
        elif (t['tile'] == 'J' and check_right(coordinate, t['coordinate']) or \
        check_top(coordinate, t['coordinate'])):
            two_tiles.append({'tile': t['tile'], 'coordinate': t['coordinate']})
        elif (t['tile'] == '7' and check_right(coordinate, t['coordinate'])):
            two_tiles.append({'tile': t['tile'], 'coordinate': t['coordinate']})
        elif (t['tile'] == 'F' and check_top(coordinate, t['coordinate'])):
            two_tiles.append({'tile': t['tile'], 'coordinate': t['coordinate']})
        
    return two_tiles

def compute_next_J(tiles, coordinate):
    two_tiles = []
    for t in tiles:
        if(t['tile'] == 'S' and (check_left(coordinate, t['coordinate']) or \
        check_top(coordinate, t['coordinate']))):
            two_tiles.append({'tile': t['tile'], 'coordinate': t['coordinate']})
        elif (t['tile'] == '-' and check_left(coordinate, t['coordinate'])):
            two_tiles.append({'tile': t['tile'], 'coordinate': t['coordinate']})
        elif (t['tile'] == '|' and check_top(coordinate, t['coordinate'])):
            two_tiles.append({'tile': t['tile'], 'coordinate': t['coordinate']})
        elif (t['tile'] == 'L' and check_left(coordinate, t['coordinate'])):
            two_tiles.append({'tile': t['tile'], 'coordinate': t['coordinate']})
        elif (t['tile'] == '7' and check_top(coordinate, t['coordinate'])):
            two_tiles.append({'tile': t['tile'], 'coordinate': t['coordinate']})
        elif (t['tile'] == 'F' and (check_top(coordinate, t['coordinate']) or \
        check_left(coordinate, t['coordinate']))):
            two_tiles.append({'tile': t['tile'], 'coordinate': t['coordinate']})
        
    return two_tiles

def compute_next_7(tiles, coordinate):
    two_tiles = []
    for t in tiles:
        if(t['tile'] == 'S' and (check_left(coordinate, t['coordinate']) or \
        check_bottom(coordinate, t['coordinate']))):
            two_tiles.append({'tile': t['tile'], 'coordinate': t['coordinate']})
        elif (t['tile'] == '-' and check_left(coordinate, t['coordinate'])):
            two_tiles.append({'tile': t['tile'], 'coordinate': t['coordinate']})
        elif (t['tile'] == '|' and check_bottom(coordinate, t['coordinate'])):
            two_tiles.append({'tile': t['tile'], 'coordinate': t['coordinate']})
        elif (t['tile'] == 'L' and (check_left(coordinate, t['coordinate']) or \
        check_bottom(coordinate, t['coordinate']))):
            two_tiles.append({'tile': t['tile'], 'coordinate': t['coordinate']})
        elif (t['tile'] == 'J' and check_bottom(coordinate, t['coordinate'])):
            two_tiles.append({'tile': t['tile'], 'coordinate': t['coordinate']})
        elif (t['tile'] == 'F' and check_left(coordinate, t['coordinate'])):
            two_tiles.append({'tile': t['tile'], 'coordinate': t['coordinate']})
        
    return two_tiles

def compute_next_F(tiles, coordinate):
    two_tiles = []
    for t in tiles:
        if(t['tile'] == 'S' and (check_right(coordinate, t['coordinate']) or \
        check_bottom(coordinate, t['coordinate']))):
            two_tiles.append({'tile': t['tile'], 'coordinate': t['coordinate']})
        elif (t['tile'] == '-' and check_right(coordinate, t['coordinate'])):
            two_tiles.append({'tile': t['tile'], 'coordinate': t['coordinate']})
        elif (t['tile'] == '|' and check_bottom(coordinate, t['coordinate'])):
            two_tiles.append({'tile': t['tile'], 'coordinate': t['coordinate']})
        elif (t['tile'] == 'L' and check_bottom(coordinate, t['coordinate'])):
            two_tiles.append({'tile': t['tile'], 'coordinate': t['coordinate']})
        elif (t['tile'] == 'J' and (check_right(coordinate, t['coordinate']) or \
        check_bottom(coordinate, t['coordinate']))):
            two_tiles.append({'tile': t['tile'], 'coordinate': t['coordinate']})
        elif (t['tile'] == '7' and check_right(coordinate, t['coordinate'])):
            two_tiles.append({'tile': t['tile'], 'coordinate': t['coordinate']})
        
    return two_tiles

@click.command()
@click.option('--file', '-f', help='Input file name.')
def maze1(file):
    """ Part 1 """
    tiles = []
    with open(file) as f:
        for x, line in enumerate(f.read().splitlines()):
            for y, col in enumerate(list(line)):
                if col == 'S':
                    start_coordinate = [x,y] # Starting point

                if col != '.':
                    tiles.append({'tile': col, 'coordinate': [x, y]})
    
    path = []
    path.append({'tile': 'S', 'coordinate': start_coordinate})
    two_tiles = compute_next_S(tiles, start_coordinate)
    tile = two_tiles[0] # arbitraty take the first one
    path.append(tile)
    i = 0
    while tile['tile'] != 'S':
        if tile['tile'] == '-':
            two_tiles = compute_next_h(tiles, tile['coordinate'])
            if two_tiles[1] == path[i]:
                tile = two_tiles[0]
            else:
                tile = two_tiles[1]
            path.append(tile)
        elif tile['tile'] == '|':
            two_tiles = compute_next_v(tiles, tile['coordinate'])
            if two_tiles[1] == path[i]:
                tile = two_tiles[0]
            else:
                tile = two_tiles[1]
            path.append(tile)
        elif tile['tile'] == 'L':
            two_tiles = compute_next_L(tiles, tile['coordinate'])
            if two_tiles[1] == path[i]:
                tile = two_tiles[0]
            else:
                tile = two_tiles[1]
            path.append(tile)
        elif tile['tile'] == 'J':
            two_tiles = compute_next_J(tiles, tile['coordinate'])
            if two_tiles[1] == path[i]:
                tile = two_tiles[0]
            else:
                tile = two_tiles[1]
            path.append(tile)
        elif tile['tile'] == '7':
            two_tiles = compute_next_7(tiles, tile['coordinate'])
            if two_tiles[1] == path[i]:
                tile = two_tiles[0]
            else:
                tile = two_tiles[1]
            path.append(tile)
        elif tile['tile'] == 'F':
            two_tiles = compute_next_F(tiles, tile['coordinate'])
            if two_tiles[1] == path[i]:
                tile = two_tiles[0]
            else:
                tile = two_tiles[1]
            path.append(tile)
        i += 1
    print(f'Result is {(len(path) - 1)//2}')

if __name__ == '__main__':
    maze1()