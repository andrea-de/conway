import numpy as np
import pandas as pd
import copy

def gen_matrix():
    x = np.random.randint(3,5)
    y = np.random.randint(3,5)
    return np.random.randint(2, size=(x, y))
    
def cycle(m):
    rows, cols = m.shape
    for i in range(rows):
        for j in range(cols):
            determine(i,j,m)

def determine(x,y,m):
    alive, dead = neighbors(x,y,m)
    cell = matrix[x][y]
    m[x][y] = calculate(cell,alive,dead)

def neighbors(x,y,m):
    neighbors = list(range(8))
    neighbors[0] = checkOnNeighbor(x+1,y+1,m)
    neighbors[1] = checkOnNeighbor(x+1,y,m)
    neighbors[2] = checkOnNeighbor(x+1,y-1,m)
    neighbors[3] = checkOnNeighbor(x-1,y+1,m)
    neighbors[4] = checkOnNeighbor(x-1,y,m)
    neighbors[5] = checkOnNeighbor(x-1,y-1,m)
    neighbors[6] = checkOnNeighbor(x,y+1,m)
    neighbors[7] = checkOnNeighbor(x,y-1,m)
    dead = neighbors.count(0)
    alive = neighbors.count(1)
    return alive, dead

def checkOnNeighbor(x,y,m):
    if(x<0 or y<0):
        return 2
    try:
        return m[x,y]
    except IndexError:
        return 2

def calculate(alive,n_alive,n_dead):
    if (alive == 0 and n_alive == 3):
        return 1
    elif (alive == 1 and (n_alive == 2 or n_alive == 3)):
        return 1
    else:
        return 0


print()
print("Original Matrix")
matrix = gen_matrix()
df1 = pd.DataFrame(np.asarray(matrix))
print(df1.to_string(index=False, header=False))
print()
    
def iterate(m):
    print()
    print("Next Iteration")
    matrixCopy = copy.copy(m)
    cycle(matrixCopy)
    df2 = pd.DataFrame(np.asarray(matrixCopy))
    print(df2.to_string(index=False, header=False))
    print()
    return matrixCopy

first = iterate(matrix)
second = iterate(first)
third = iterate(second)
iterate(third)