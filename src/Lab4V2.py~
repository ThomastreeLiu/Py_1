#%% LAB 4  ENCMP 100 Computer Programming for Engineers
#
# Student name:
# Student CCID:
# Others:
#
# To avoid plagiarism, list the names of others, Version 0 author(s)
# aside, whose code, words, ideas, images, or data you incorporated.
# To avoid unauthorized collaboration, list all others, excluding
# lab instructor and TAs, who gave compositional assistance.
#
# After each name, including your own name, enter in parentheses an
# estimate of the source's contributions in percent. Supply these
# numbers, which must add to 100%, to receive a nonzero mark.
#
# For obscure and anonymous or known and non-human sources, enter
# pseudonyms or names in uppercase, e.g., DARKWEB or CHATGPT, followed
# by percentages. Send one email to the lab instructor with copies of
# obscure and anonymous sources when you submit your assignment.
#
#%% TSPANALYZE  Geomatics and the Travelling Sales[person] Problem
#
# According to the ISO/TC 211, geomatics is the "discipline concerned
# with the collection, distribution, storage, analysis, processing, [and]
# presentation of geographic data or geographic information." Geomatics
# is associated with the travelling salesman problem (TSP), a fundamental
# computing problem. In this lab assignment, a University of Alberta
# student completes a Python program to analyze, process, and present
# entries, stored in a binary data file, of the TSPLIB, a database
# collected and distributed by the University of Heidelberg.
#
# Copyright (c) 2024, University of Alberta
# Electrical and Computer Engineering
# All rights reserved.
#
import scipy.io as io
import numpy as np

tsp = io.loadmat('tspData.mat', squeeze_me=True)
tsp = np.ndarray.tolist(tsp['tsp'])
file = open('tspAbout.txt', 'r')
print(file.read())
file.close()
print()
print("MAIN MENU")
print("0. Exit program")
print("1. Print database")
print("2. Limit dimension")
print("3. Plot one tour")
print()
choice = int(input("Choice (0-3)? "))
while choice < 0 or choice > 3:
    choice = int(input("Choice (0-3)? "))
while choice != 0:
    if choice == 1:
        print()
        print("NUM  FILE NAME  EDGE TYPE  DIMENSION  COMMENT")
        for k in range(1, len(tsp)):
            name = tsp[k][0]
            edge = tsp[k][5]
            dimension = tsp[k][3]
            comment = tsp[k][2]
            print("%3d  %-9.9s  %-9.9s  %9d  %s"
                  % (k, name, edge, dimension, comment))
    elif choice == 3:
        num = int(input("Number (EUC_2D)? "))
        edge = tsp[num][5]
        if edge == 'EUC_2D':
            print("Valid (%s)!!!" % edge)
        else:
            print("Invalid (%s)!!!" % edge)
    print()
    print("MAIN MENU")
    print("0. Exit program")
    print("1. Print database")
    print("2. Limit dimension")
    print("3. Plot one tour")
    print()
    choice = int(input("Choice (0-3)? "))
    while choice < 0 or choice > 3:
        choice = int(input("Choice (0-3)? "))
