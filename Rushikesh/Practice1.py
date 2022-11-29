# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 20:21:22 2022

@author: Rush
@AIM: Get points lie in the line formed by two point form
i/p: (x1,y1), (x2,y2), N
o/p: [(a1,b1), (a2,b2),...(an,bn)]
y = mx + c ...Use two point form
m = (y2-y1)/(x2-x1)
c =  -m*x1 + y1
"""

import numpy as np


x1 = 1
y1 = 2
x2 = 102
y2 = 103
N = 100
m = 1
c = 1

# x1 = input("Enter co-ords of A:")
# print(x1,y1)

def cal_tpl(ar_x, m, c):
    ar_y = []
    for i in ar_x:
        y = m*i + c
        ar_y.append(y)
    line_tuple= list(zip(ar_x,ar_y))
    return line_tuple

def get_points(x1, y1, x2, y2, N):

    m = (y2-y1)/(x2-x1)
    c =  -(m*x1) + y1
    line_x = np.linspace(x1, x2, N+1, endpoint=False)[1:]

    line_tuple = cal_tpl(line_x, m, c)
    
    point_x = np.arange(-50, 51)
    point_tuple = cal_tpl(point_x, m, c)
    return point_tuple, line_tuple 

# point_x = np.arange(-50, 51)
# point_tuple = cal_tpl(point_x, m, c)

# IMPLEMENT
result = get_points(1,2,102,103,100)
print("required output" ,result[1])
print("---------------------------")
print("line drawn: ", result[0])