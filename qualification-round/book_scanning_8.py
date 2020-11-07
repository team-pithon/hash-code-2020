#import numpy
#import math
import random
from sys import argv

class Library:
    def __init__(self, id, nbooks, rate, ndays, book_list, maxbooks):
        self.id = id
        self.nbooks = nbooks
        self.rate = rate
        self.ndays = ndays
        self.book_list = book_list
        self.maxbooks = 0

libraries = []

#opening the input file
with open(argv[1]+".txt", 'r') as f_in:
    #setting the input variables
    first_line = f_in.readline()
    total_books, total_libraries, total_days = [int(n) for n in first_line.split()]
    max_ndays = total_days
    min_ndays = total_days
    books_score = f_in.readline()
    books_score = [int(n) for n in books_score.split()]
    #print(books_score)
    for i in range(total_libraries):
        line = f_in.readline()
        nbooks, ndays, rate = [int(n) for n in line.split()]
        line = f_in.readline()
        book_list = [(int(n), books_score[int(n)]) for n in line.split()]
        book_list.sort(key = lambda x: x[1], reverse=True)
        book_list = [x[0] for x in book_list]
        libraries.append(Library(i, nbooks, rate, ndays, book_list, 0))

#libraries.sort(key=lambda x: x.ndays)
#new_libraries = sorted(libraries, key=lambda x: x.ndays)
#lib_ids = range(total_libraries)


libs = [(x.id,len(x.book_list)) for x in libraries]
libs.sort(key = lambda x: x[1])
libs = [x[0] for x in libs]

#print(libs)

nlib = 0
days_passed = 0
for i in range(total_libraries):
    if days_passed + libraries[libs[i]].ndays <= total_days:
        nlib+=1
        days_passed += libraries[libs[i]].ndays
    else:
        break




with open(argv[1]+".out", 'w') as f_out:
    books_digit = []
    days_passed = 0
    og_nlib = nlib
    for i in range(nlib):
        libraries[libs[i]].maxbooks = (total_days - days_passed - libraries[libs[i]].ndays) * libraries[libs[i]].rate
        libraries[libs[i]].book_list[:libraries[libs[i]].maxbooks]
        libraries[libs[i]].book_list = [item for item in libraries[libs[i]].book_list if item not in books_digit]
        books_digit = books_digit + libraries[libs[i]].book_list
        days_passed += libraries[libs[i]].ndays
        if len(libraries[libs[i]].book_list) == 0:
            nlib-=1
        if len(libraries[libs[i]].book_list) != 0:
            f_out.write(str(libs[i]) + ' ' + str(len(libraries[libs[i]].book_list)) + '\n')
            for j in range(len(libraries[libs[i]].book_list)):
                f_out.write(str(libraries[libs[i]].book_list[j]) + ' ')
            f_out.write('\n')

#We read the existing text from file in READ mode
src=open(argv[1]+".out","r")
fline=str(nlib)+'\n'    #Prepending string
oline=src.readlines()
#Here, we prepend the string we want to on first line
oline.insert(0,fline)
src.close()


#We again open the file in WRITE mode
src=open(argv[1]+".out","w")
src.writelines(oline)
src.close()
