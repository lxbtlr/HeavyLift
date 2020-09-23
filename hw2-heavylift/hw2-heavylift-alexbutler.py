import math
import random 
import re
import numpy as np
import matplotlib.pyplot as plt


#   Script made to find the average consecutive carry bits for n-bit addition
#   from input bits, generates list of 10k random operand pairs [range 0-(2^n-1)]
#   performs addiiton of the numbers and finds the longest stretch of consecutive carry bits from the addition.

'''
    Average Consecutive Carry Bits (10k samples):
        4-bits  = ~0.879
        8-bits  = ~1.307
        12-bits = ~1.576
        14-bits = ~1.669
        16-bits = ~1.760
        32-bits = ~2.211
'''

def Runner(a,b,bits):
    newa = bin(a)[2:]
    newa = newa.zfill(bits)
    newb = bin(b)[2:]
    newb = newb.zfill(bits)[:]
    
    return carrys(bits, newa,newb)

def carrys(bits, na,nb):
    if bits <= 0:
        return ""
    # print(bits, na, nb)
    summy = int(na[-1])+int(nb[-1])
    
    if summy <= 1:
        return carrys(bits-1,na[0:-1],nb[0:-1])+ "0"
    if summy >= 2:
        return carrys(bits-1,na[0:-1],nb[0:-1])+ "1"

while True:
    try:
        bits = int(input("number of bits 8,10,12,14,16..."))
        break
    except:
        print("That's not a valid int")

listy = [[0 for x in range(10000)] for y in range(2)] 

for i in range(0,len(listy)):
    for k in range(0,len(listy[i])):
        listy[i][k] = random.randint(0,(2**bits)-1) 

fig, axs = plt.subplots(2)
fig.suptitle('Distribution of Random Operands')
axs[0].hist(listy[0])
axs[1].hist(listy[1])

# distribution of the random operands
# plt.show()

carryouts = []

# # proof that the system works
# print(Runner(listy[0][0],listy[1][0],bits))

for q in range(len(listy[1])):
    carryouts.append(Runner(listy[0][q],listy[1][q],bits))

#outputs from the carry of the n-bit adder
# print(carryouts)

# find longest consecutive run of 1s
con1s = []

for i in carryouts:
    con1s.append(len(max(re.compile("1*").findall(i))))

print(sum(con1s)/len(con1s))
print()
print("List of Average Consecutive Carry Outs from common n-bits:")
print(" 4-bits  = ~0.879 \n8-bits  = ~1.307 \n12-bits = ~1.576 \n14-bits = ~1.669 \n16-bits = ~1.760 \n32-bits = ~2.211")
input()