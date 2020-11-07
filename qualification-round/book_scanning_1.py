#import numpy
#import math
from sys import argv

class Library:
    def __init__(self, id, nbooks, rate, ndays, book_list):
        self.id = id
        self.nbooks = nbooks
        self.rate = rate
        self.ndays = ndays
        self.book_list = book_list


libraries = []

#opening the input file
with open(argv[1]+".txt", 'r') as f_in:
    #setting the input variables
    first_line = f_in.readline()
    total_books, total_libraries, total_days = [int(n) for n in first_line.split()]
    books_score = f_in.readline()
    books_score = [int(n) for n in first_line.split()]
    for i in range(total_libraries):
        line = f_in.readline()
        nbooks, ndays, rate = [int(n) for n in line.split()]
        line = f_in.readline()
        book_list = [int(n) for n in line.split()]
        libraries.append(Library(i, nbooks, ndays, rate, book_list))

nlib = 0
days_passed = 0
for Library in libraries:
    if days_passed + Library.ndays <= total_days:
        nlib+=1
        days_passed += Library.ndays
    else:
        break

with open(argv[1]+".out", 'w+') as f_out:
    f_out.write(str(nlib)+'\n')
    for i in range(nlib):
        f_out.write(str(i) + ' ' + str(libraries[i].nbooks) + '\n')
        for j in range(len(libraries[i].book_list)):
            f_out.write(str(libraries[i].book_list[j]) + ' ')
        f_out.write('\n')
