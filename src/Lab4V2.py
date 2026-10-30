#%% LAB 4  ENCMP 100 Computer Programming for Engineers
#
# Student name:Thomas Liu
# Student CCID:shuyi19
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
import matplotlib.pyplot as plt


def main():
    tsp = io.loadmat('tspData.mat', squeeze_me=True)
    tsp = np.ndarray.tolist(tsp['tsp'])

    file = open('tspAbout.txt', 'r')
    print(file.read())
    file.close()

    choice = menu()
    while choice != 0:
        if choice == 1:
            tspPrint(tsp)
        elif choice == 2:
            tspLimit(tsp)
        elif choice == 3:
            tspPlot(tsp)
        choice = menu()


def menu():
    # Purpose: Display the menu and read a valid choice.
    # Input: None.
    # Output: choice, an integer from 0 to 3.
    # Side effects: Prints menu text and reads console input.
    print()
    print('MAIN MENU')
    print('0. Exit program')
    print('1. Print database')
    print('2. Limit dimension')
    print('3. Plot one tour')
    print()
    choice = int(input('Choice (0-3)? '))
    while choice < 0 or choice > 3:
        choice = int(input('Choice (0-3)? '))
    return choice


def tspPrint(tsp):
    # Purpose: Print all current TSP records in a table.
    # Input: tsp, a list containing the database header and records.
    # Output: None.
    # Side effects: Prints a table to the console.
    print()
    print('NUM  FILE NAME  EDGE TYPE  DIMENSION  COMMENT')
    for k in range(1, len(tsp)):
        name = tsp[k][0]
        edge = tsp[k][5]
        dimension = tsp[k][3]
        comment = tsp[k][2]
        print('%3d  %-9.9s  %-9.9s  %9d  %s'
              % (k, name, edge, dimension, comment))


def tspMinMax(tsp):
    # Purpose: Find the smallest and largest dimensions in the database.
    # Input: tsp, a list of TSP records with a header at index 0.
    # Output: minVal and maxVal, two integer dimensions.
    # Side effects: None.
    minVal = tsp[1][3]
    maxVal = tsp[1][3]
    for k in range(2, len(tsp)):
        dimension = tsp[k][3]
        if dimension < minVal:
            minVal = dimension
        if dimension > maxVal:
            maxVal = dimension
    return minVal, maxVal


def tspLimit(tsp):
    # Purpose: Remove TSP records whose dimensions exceed a chosen limit.
    # Input: tsp, a mutable list of TSP records.
    # Output: None; the same tsp list is modified in place.
    # Side effects: Prints the dimension range, reads input, deletes records.
    minVal, maxVal = tspMinMax(tsp)
    print('Min dimension:', minVal)
    print('Max dimension:', maxVal)
    limit = int(input('Limit value? '))
    while limit < minVal or limit > maxVal:
        limit = int(input('Limit value? '))

    for k in range(len(tsp) - 1, 0, -1):
        if tsp[k][3] > limit:
            del tsp[k]


def tspPlot(tsp):
    # Purpose: Select a record and plot it when its edge type is EUC_2D.
    # Input: tsp, a list of TSP records.
    # Output: None.
    # Side effects: Reads input, may print an error, and may create a plot.
    num = int(input('Number (EUC_2D)? '))
    while num < 1 or num >= len(tsp):
        num = int(input('Number (EUC_2D)? '))

    tsp1 = tsp[num]
    edge = tsp1[5]
    if edge == 'EUC_2D':
        plotEuc2D(tsp1[10], tsp1[2], tsp1[0])
        print('See tspPlot.png')
    else:
        print('Invalid (%s)!!!' % edge)


def plotEuc2D(coord, comment, name):
    # Purpose: Draw a 2D tour, joining the final point to the first.
    # Input: coord (NumPy coordinate array), comment, and name.
    # Output: None.
    # Side effects: Displays a plot and saves it as tspPlot.png.
    x = coord[:, 0]
    y = coord[:, 1]

    plt.figure()
    plt.plot(x, y, 'b.-', label=name)

    xClose = [x[-1], x[0]]
    yClose = [y[-1], y[0]]
    plt.plot(xClose, yClose, 'r-')

    plt.title(comment)
    plt.xlabel('x-Coordinate')
    plt.ylabel('y-Coordinate')
    plt.legend()
    plt.savefig('tspPlot.png')
    plt.show()


main()
