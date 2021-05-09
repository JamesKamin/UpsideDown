#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 16:30:11 2021

@author: jkenglish
"""

def reverse(x): 
    if len(x) == 0: 
        return x 
    else: 
        return reverse(x[1:]) + x[0] 
  
x = "rood tsae krad pleh tsohg"
  

print (end="") 
print (reverse(x)) 

