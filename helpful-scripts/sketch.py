#import numpy
#import math
from sys import argv #used for getting desired input and output file names from the command line (shell script in this case)

#opening the input file
with open(argv[1], 'r') as f_in:
    #setting the input variables
    first_line = f_in.readline()
    row_count, column_count, var3, var4 = [int(n) for n in first_line.split()]

    #creating the grid and populating it
    grid = []
    for i in range(row_count):
        grid.append(f_in.readline().rstrip())

		
		
		
		
global_counter = 0		
f_out = open(argv[2]+"_temp.out",'w+')

if len([list_index[2])==1:
	f_out.write('%s\n' % ([list_index[2][0]))
else:
	f_out.write('%s %s\n' % ([list_index[2][0], [list_index[2][1]))))


f_out.close()

with open(argv[2]+"_temp.out", 'r') as f_temp:
    with open(argv[2], 'w+') as f_out:
        f_out.write(str(global_counter)+'\n')
        for line in f_temp:
            f_out.write(line)
