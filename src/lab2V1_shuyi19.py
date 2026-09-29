#%% LAB 2  ENCMP 100 Computer Programming for Engineers
#
# Student name: Thomas Liu
# Student CCID: 1964824
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
#%% DECODE  Steganography, Detecting and Decoding a Secret Message
#
# Steganography has been used over millennia to hide information in
# plain sight. This assignment concerns the determination of a secret
# message, about an international rescue, from a list of university
# phone numbers. Each student writes a script to detect if a number
# likely represents a message and, if so, to decode the secret.
#
# Copyright (c) 2024, University of Alberta
# Electrical and Computer Engineering
# All rights reserved.
#
import numpy as np

#%% PARSE INPUT
#
numstr = input("Enter a number to check")
validate = True
if (len(numstr) != 11):
    print("Not eleven digits")
    validate = False
    exit()

test_string_first = 0
for i in range(0, 5):
    test_string_first = test_string_first + int(numstr[i])
test_string_last = 0
for i in range(6, 11):
    test_string_last = test_string_last + int(numstr[i])

if(test_string_first % 2 == 1 or test_string_last % 2 == 1):
    validate = False
    print("A digit sum is odd")

if not validate:
    exit()


