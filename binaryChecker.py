#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 17:12:21 2017

@author: ChrisErnst
"""

def binaryChecker():
    
    print("Please enter number to be converted to binary: ")
    try:
        num = eval(input())

        binNum = bin(num)[2:]
        
        print("\n\n",num, " in binary is: ", binNum , "\n")
        
        zeroPlace = int(binNum[-1])
        
        if zeroPlace == 0:
            print("This is an even number\n\n\n")
        elif zeroPlace == 1:
            print("This is an odd number!\n\n\n")
        print("That's because...\n\n")
        
        binaryLength = len(binNum)
        
        if binaryLength == 1:
            print(binNum,"multiplied by 2^0", " is ", binNum )
        
        else:
            print(binNum[-1], "multiplied by 2^0 is ", binNum[-1]*2**0)
            for p in range(2,binaryLength+1):
                print(binNum[-p],"multiplied by 2^", p-1, " is ", int(binNum[-p]) * 2**(p-1))
            print("________________________________+\n")
            print(".........................", num)
    
    except:
        print("Please enter an integer!")
                
                



