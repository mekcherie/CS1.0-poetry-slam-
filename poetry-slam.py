# import random
from random import randint 


def get_file_lines(filename):
    # "R" it means read
    # reading it and putting in a list 
        in_file = open(filename, "r")
    # if you put a number inside the bracket it will print out the line only 
        lines = in_file.readlines()
        in_file.close()
        return lines 

# printing it backwards
def lines_printed_backwards(lines_list):
    # this reverses a list 
    lines_list.reverse()
    lines_length = len(lines_list)
    for i in range (lines_length):
        line = lines_list[i]
        line_num = lines_length - i
        print(f"{line_num} {line}")
    print('-----------')

# printing it randomly 
def lines_printed_random(lines_list): 
        for _ in range(len(lines_list)):
            # print(i)
            print(lines_list[randint(0,13)])
        print('-----------')

            # pass 

# printing it by custom 
# print out even lines 
def lines_printed_custom(lines_list):

    for i in range(len(lines_list)):
        # i=value
        # if i divded by two is the remandinder of 
        if i % 2 == 0:
             print(lines_list[i])

    print('-----------')


poem_lines = get_file_lines('poem.txt')
print(poem_lines)


lines_printed_backwards(poem_lines)

lines_printed_random(poem_lines)

lines_printed_custom(poem_lines)

