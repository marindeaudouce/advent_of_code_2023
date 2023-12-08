import click
from functools import cmp_to_key

strength = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

def compare(item1, item2):
    if item1['type'] < item2['type']:
        return -1
    elif item1['type'] > item2['type']:
        return 1
    else:
        ord_item1 = [strength.index(c) for c in item1['cards']]
        ord_item2 = [strength.index(c) for c in item2['cards']]
        return [b - a for a, b in zip(ord_item1, ord_item2) if b - a != 0][0]

@click.command()
@click.option('--file', '-f', help='Input file name.')
def camel1(file):
    """ Part 1 """
    all_cards = []
    with open(file) as f:
        for line in f.read().splitlines():
            cards, bid = line.split(' ')
            cards_no_dup = "".join(set(cards))
            if len(cards_no_dup) == 1:
                # Five of 
                all_cards.append({'cards': cards, 'bid': int(bid), 'type': 7})
            elif len(cards_no_dup) == 2:
                enum1 = 0
                enum2 = 0
                for c in cards:
                    if cards_no_dup[0] == c:
                        enum1 += 1
                    elif cards_no_dup[1] == c: 
                        enum2 += 1
                if enum1 == 4 or enum2 == 4:
                    # Four of
                    all_cards.append({'cards': cards, 'bid': int(bid), 'type': 6})
                else:
                    # Full house
                    all_cards.append({'cards': cards, 'bid': int(bid), 'type': 5})
            elif len(cards_no_dup) == 3:
                enum1 = 0
                enum2 = 0
                enum3 = 0
                for c in cards:
                    if cards_no_dup[0] == c:
                        enum1 += 1
                    elif cards_no_dup[1] == c:
                        enum2 += 1 
                    elif cards_no_dup[2] == c:
                        enum3 += 1
                if enum1 == 3 or enum2 == 3 or enum3 == 3:
                    # Three of 
                    all_cards.append({'cards': cards, 'bid': int(bid), 'type': 4})
                else:
                    # Two pair
                    all_cards.append({'cards': cards, 'bid': int(bid), 'type': 3})
            elif len(cards_no_dup) == 4:
                # One pair
                all_cards.append({'cards': cards, 'bid': int(bid), 'type': 2})
            elif len(cards_no_dup) == 5:
                # High card
                all_cards.append({'cards': cards, 'bid': int(bid), 'type': 1})
            else:
                print(f'ERROR {cards_no_dup}')
            
    all_cards.sort(key=cmp_to_key(compare))
    print(all_cards)

    res = 0
    for idx, c in enumerate(all_cards):
       res += (idx + 1)*c['bid'] 

    print(res)

if __name__ == '__main__':
    camel1()