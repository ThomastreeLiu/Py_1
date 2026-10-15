#%% LAB 3  ENCMP 100 Computer Programming for Engineers
#
# Student name: Thomas Liu
# Student CCID: shuyi19
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
#%% SAVINGS  Education Savings, Cash Flow and Compound Interest
#
# With the help of a Registered Education Savings Plan (RESP), parents
# or guardians can save regularly for a child's university education
# without paying tax on interest earned. Long term investments can
# also leverage higher interest rates and the compounding of interest
# available from major lenders. In this lab assignment, a university
# student investigates an education savings plan and compares it to
# anticipated tuition fees, considering fee increases.
#
# Copyright (c) 2025, University of Alberta
# Electrical and Computer Engineering
# All rights reserved.
#
import numpy as np
import matplotlib.pyplot as plt

#%% CASH OUTFLOW
#
print("Please enter the total fees in 18 years ($):")
totalFee = float(input(""))

#%% CASH INFLOW
#
balance = np.zeros(18 * 12)
print("Please enter the initial savings amount ($):")
balance[0] = float(input(""))

#%% CHECK SAVINGS
#
print("Please enter the monthly savings amount in $")
monthly_saving = float(input(""))
print ("Please enter the annual interest rate in %")
annual_rate = float(input(""))

for i in range(1, 216):
    interest = balance[i - 1] * annual_rate / 1200
    balance[i] = balance[i - 1] + interest + monthly_saving

if balance[215] >= totalFee:
    print("Congratulations! You have saved enough.")
else:
    print("Unfortunately, you have not saved enough.")
#%% PLOT AMOUNTS
#
years = np.arange(216) / 12

plt.plot(years, balance, label="Savings")
plt.axhline(y = totalFee, label = "Tuition Fees", color = "red")
plt.xticks(np.arange(0, 19, 2))
plt.xlim(0, 18)

plt.xlabel("Year")
plt.ylabel("Amount ($)")
plt.legend()
plt.show()
