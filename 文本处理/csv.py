import numpy
from numpy import *
import numpy as np

def Maze():

    maze = array([[2,2,2,2,2,2,2],
                 [2,0,0,0,0,0,2],
                 [2,0,2,0,2,0,2],
                 [2,0,0,2,0,2,2],
                 [2,2,0,2,0,2,2],
                 [2,0,0,0,0,0,2],
                 [2,2,2,2,2,2,2]])

    startI = 1
    startJ = 1
    endI = 5
    endJ = 5
    success = 0
    print('显示迷宫：\n')
    for i in range(0,7):
        for j in range(0,7):
            if maze[i,j] == 2:
                print('#')
            else:
                print('  ')
        print('\n')



#费氏数列
def Fib(N):
    fib=[]
    fib.insert(0,0)
    fib.insert(1,1)
    for i in range(2,N):
        fib.insert(i,fib[i-1]+fib[i-2])
    for i in range(1,N):
        print(fib[i])




if __name__ == '__main__':
    Fib(20)
    Maze()
