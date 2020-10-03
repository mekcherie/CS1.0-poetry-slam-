import random
from random import randint 
even_lines = []
def get_file_lines(filename):
    # "R" it means read
    # reading it and putting in a list 
    in_file = open(filename, "r")
    lines = in_file.readlines()
    in_file.close()
    return lines 

# printing it backwards
# def lines_printed_backwards(lines_list):
#     # this reverses a list 
#     lines_list.reverse()
#     lines_length = len(lines_list)
#     for i in range (lines_length):
#         line = lines_list[i]
#         line_num = lines_length - i
#         print(f"{line_num} {line}")

# printing it randomly 
def lines_printed_random(lines_list): 
    import random 
    lines_list = random.randint(1, 3)
    print(lines_list)
    # lines_list = ['coffee', 'Ethiopia', 'heal', 'land']
    # for i in range(10):
        
    #     print random.randint(1,6) *2
    #     print 
    # print("Random element from list:", random.choice(lines_list))
    pass 

# printing it by custom 
# print every line divided with 4
# def lines_printed_custom(lines_list):
#     lines_length = len(lines_list)
#     for i in range(lines_length):
#         if i % 4 == 0:
#             print(lines_list[i])

# print even lines
    # even_length = len(even_lines)
    # for index in range(even_length):
    #     print(even_lines[index], end="")

poem_lines = get_file_lines('poem.txt')
# print(poem_lines)


# lines_printed_backwards(poem_lines)

lines_printed_random(poem_lines)

# lines_printed_custom(poem_lines)

