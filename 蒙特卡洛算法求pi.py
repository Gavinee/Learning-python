"""
利用蒙特卡洛投针实验来进行pi的计算
"""

__author__ = Qiufeng


#程序一
import random
import math

def ifPi(x,y,count):
    if pow(x,2) +pow(y,2) >1:
        return count
    else:
        count[0] = count[0]+1
    return count

def calculatePi(nums):
    count = [0]
    i = 0
    while(i<nums):
        ifPi(random.random(),random.random(),count)
        i = i+1
    pi = 4*count[0]/nums
    return pi

nums = 10000000
pi = calculatePi(nums)
print(pi)


#程序2
from random import random
from math import sqrt
from time import clock

DARTS = 10000
hits = 0.0
clock()

for i in range(1,DARTS+1):
    x,y = random(),random()
    dist = sqrt(x**2+y**2)
    if dist <= 1.0:
        hits = hits + 1
pi = 4*(hits/DARTS)
print("Pi的值{}.".format(pi))
print("运行时间是:{:5.5}s".format(clock()))
