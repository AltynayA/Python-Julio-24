#!/usr/bin/python
import math
def displayPathtoPrincess(n,grid):
    m1 = None
    m2 = None
    p1 = None
    p2 = None
    for i in range(n):
        for j in range(n):
            if grid[i][j] == "m":
                m1 = i
                m2 = j
            elif grid[i][j] == "p":
                p1 = i
                p2 = j
    if m1 != p1:
        if m1 < p1:
            for i in range(abs(p1 - m1)):
                print("DOWN") 
        else:
            for i in range(abs(p1 - m1)):
                print("UP") 
    if m2 != p2:
        if m2 < p2:
            for i in range(abs(p2 - m2)):
                print("RIGHT") 
        else:
            for i in range(abs(p2 - m2)):
                print("LEFT") 

    

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)s