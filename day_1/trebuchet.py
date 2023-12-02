import click
import re

@click.command()
@click.option('--file', '-f', help='Input file name.')
def trebuchet1_v1(file):
    """ Part 1: Stupid way """
    with open(file) as f:
        lines = f.readlines()
        sum = 0
        for line in lines:
            for i in line:
                if(i.isdigit()):
                    number1 = int(i)
                    break
            for j in line[::-1]:
                if(j.isdigit()):
                    number2 = int(j)
                    break
            sum += number1*10 + number2
        print('Result is', res)

@click.command()
@click.option('--file', '-f', help='Input file name.')
def trebuchet1_v2(file):
    """ Part 1: Maybe more clever way """
    with open(file) as f:
        res = 0
        for line in f.readlines():
            digit_list = list(filter (lambda test: test.isdigit(), line))
            res += int(digit_list[0] + digit_list[-1])
        print('Result is', res)

@click.command()
@click.option('--file', '-f', help='Input file name.')
def trebuchet2(file):
    """ Part 2 """
    valid_digits = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    with open(file) as f: 
        res = 0
        for line in f.readlines():
            # Replace the spelled number by a real digit
            for valid_digit in valid_digits.keys():
                if line.find(valid_digit) != -1:
                    # Morgan's tick when spelled numbers share some letters
                    line = line.replace(valid_digit, valid_digit + valid_digits[valid_digit] + valid_digit)

            # Same as Part 1
            digit_list = list(filter (lambda test: test.isdigit(), line))
            res += int(digit_list[0] + digit_list[-1])

        print('Result is', res)

@click.command()
@click.option('--file', '-f', help='Input file name.')
def trebuchet2_v2(file):
    """ Part 2 """
    valid_digits = {'one':'1', '1':'1', 'two':'2', '2':'2', 'three':'3', '3':'3', 'four':'4', '4':'4', 'five':'5', '5':'5', 'six':'6', '6':'6', 'seven':'7', '7':'7', 'eight':'8', '8':'8', 'nine':'9', '9':'9'}
    with open(file) as f: 
        res = 0
        for line in f.readlines():
            digit_dict = dict()
            # Get the index where each spelled digits appears
            for spelled_digit in valid_digits.keys():
                for idx in re.finditer(spelled_digit, line):
                    digit_dict[idx.start()] = valid_digits[spelled_digit]
            
            first_idx = min(digit_dict.keys())
            last_idx = max(digit_dict.keys())
            res += int(digit_dict[first_idx] + digit_dict[last_idx])

        print('Result is', res)

if __name__ == '__main__':
    trebuchet2_v2()