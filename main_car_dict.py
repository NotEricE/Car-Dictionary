"""Importing the dictionaries in to one location"""
from bmw_dict import bmw
from audi_dict import audi
from benz_dict import benz
from chevy_dict import chevy
from nissan_dict import nissan
from ford_dict import ford
from honda_dict import honda
from porsche_dict import porsche
"""This prints out the dictionaries in a neat format"""
from neat import print_neat

"""This loop will keep on prompting the user for input
 and print out a dictionary till the user quits the loop"""
while True:
    i = input("What car make are you looking for? ")
    print("Enter 'q' to quit at any time")
    u = i.upper()

    if u == 'Q':
        break
    if u == 'BMW':
        print_neat(bmw)
    elif u == 'PORSCHE':
        print_neat(porsche)
    elif u == 'NISSAN':
        print_neat(nissan)
    elif u == 'CHEVY':
        print_neat(chevy)
    elif u == 'CHEVROLET':
        print_neat(chevy)
    elif u == 'FORD':
        print_neat(ford)
    elif u == 'BENZ':
        print_neat(benz)
    elif u == 'MERCEDES':
        print_neat(benz)
    elif u == 'MERCEDES BENZ':
        print_neat(benz)
    elif u == 'AUDI':
        print_neat(audi)
    elif u == 'HONDA':
        print_neat(honda)