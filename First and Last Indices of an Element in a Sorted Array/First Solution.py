#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 17:19:05 2019

@author: gauravmalik
"""
class Solution: 
    def getRange(self, arr, target):
        print(arr, target)
        firstPos = -1
        lastPos = -1
        for i in range(len(arr)):
            if arr[i]==target:
                if firstPos == -1:
                    firstPos = i
                else:
                    lastPos = i
        return [firstPos, lastPos]
  
# Test program 
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
x = 2
print(Solution().getRange(arr, x))
# [1, 4]

arr = [1,3,3,5,7,8,9,9,9,15]
x = 9
print(Solution().getRange(arr, x))
#[6,8]

arr = [100, 150, 150, 153]
x = 150
print(Solution().getRange(arr, x))
#[1,2]

arr = [1,2,3,4,5,6,10]
x = 9
print(Solution().getRange(arr, x))
#[-1,-1]
