'''
  template for handeling the input from file
  using in codejam, hashcode etc.
 '''
 
import argparse
import logging
import sys
import os
def compute(des,ids_list):
    print("We perform some computation here!")
    print(des)
    print(ids_list)
    res = des + ids_list
    return res

def parse_output(file_out):
    """
    :param file_out: output file name (solution)
    """
    print("writing in a file")
    output = open("../output.txt", "a+")
    for i in file_out:
        output.write(str(i))
    output.close()    

def parse_input(file_in):
    """
    Parse input file
    :param file_in: input file name
    """
#     logging.debug("parsing {}".format(file_in))
    with open(file_in, 'r') as f:
        first_line = f.readline()
        print("---", first_line)
        total_books, libs, days = first_line.split(' ')
        score = list(map(int, f.readline().split(' ')))
        print("$$", score)
        lib_desc = []
        ids = []
        for lib in range(int(libs)):
            info = list(map(int,f.readline().split(' ')))
            lib_desc.append(info)
            ids.append(list(map(int,f.readline().split(' '))))
    
#     logging.debug("parsing {}: done".format(file_in))
    return lib_desc , ids

        
def main():
    #parse input
    lib_des , ids = parse_input("../A.txt")
    
    #compute some 
    res = compute(lib_des, ids)
    
    #write in file "output.txt"
    parse_output(res)
    
if __name__ == '__main__':
    main()
