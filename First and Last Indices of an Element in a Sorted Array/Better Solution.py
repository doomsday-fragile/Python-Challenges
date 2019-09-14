#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 17:19:05 2019

@author: gauravmalik
"""
class Solution: 
    """This class contains a method called *getRange* which returns the first and last pos of target element in arr"""
    def getRange(self, arr, target):
        firstPos, lastPos = -1, -1
        if target in arr:
            firstPos = arr.index(target)
            lastPos = len(arr) - 1 - arr[::-1].index(target)
            if lastPos == firstPos:
                lastPos = -1
        return [firstPos, lastPos]
  
# Test program 
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
x = 2
print(Solution().getRange(arr, x))
#Desired Output [1, 4]

arr = [1,3,3,5,7,8,9,9,9,15]
x = 9
print(Solution().getRange(arr, x))
#Desired Output [6,8]

arr = [100, 150, 150, 153]
x = 150
print(Solution().getRange(arr, x))
#Desired Output [1,2]

arr = [1,2,3,4,5,6,10]
x = 9
print(Solution().getRange(arr, x))
#Desired Output [-1,-1]
