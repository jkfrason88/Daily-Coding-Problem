# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 00:14:20 2021

@author: jkfra
"""

given_list = [1,2,3,4,5]

def compute(a_list):
    new_list = []
    
    for index, value in enumerate(a_list):
        orignal_list = a_list
        orignal_int = orignal_list[index]
        orignal_list[index] = 1
        
        result = 1
        for x in orignal_list:
            result = result * x
            
        new_list.append(result)
        
        orignal_list[index] = orignal_int
    return new_list

r = compute(given_list)
print(r)