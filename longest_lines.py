# Reads a file
# Prints to stdout
# specified number (n)
# of longest lines
# sorted by length in descending order

import sys

def print_longest_lines(data):
    data = file.read()
    lines = data.split("\n")
    n = int(lines[0])
    i = 1
    line_lengths = []
    
    for line in lines[1:]:
        tpl = (i, len(line))
        line_lengths.append(tpl)
        i += 1

    sorted_lines = sorted(line_lengths, key=lambda line: line[1])

    x = 0
    longest_lines = ""
    
    while x < n:
        index, length = sorted_lines.pop()
        longest_lines += "{}\n".format(lines[index])
        x +=1
        
    return longest_lines

file = open(sys.argv[1], 'r')
sys.stdout.write(print_longest_lines(file))
file.close()
