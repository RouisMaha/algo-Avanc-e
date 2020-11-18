#!/usr/bin/env python
# coding: utf-8

# In[85]:


import random
import math
import matplotlib.pyplot as plt


# In[86]:


import numpy as np
board=[[]]
print ('Veuillez entrer la taille du echiquier : ')
n = input()
board=np.random.randint(n, size=(4,4))
print(board)
m=board.size
print(m)


# In[87]:


def isSafe(board, row, col): 
  
    # Check this row on left side 
    N=4
    for i in range(col): 
        if board[row][i] == 1: 
            return False
        
    # Check upper diagonal on left side 
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)): 
        if board[i][j] == 1: 
            return False
  
    # Check lower diagonal on left side 
    for i, j in zip(range(row, N, 1), range(col, -1, -1)): 
        if board[i][j] == 1: 
            return False
  
    return True


# In[88]:


isSafe(board, 2, 2)


# In[89]:


def Deplacer(board, col): 
    # base case: If all queens are placed 
    # then return true
    N=4
    if col >= N: 
        return True
  
    # Consider this column and try placing 
    # this queen in all rows one by one 
    for i in range(N): 
  
        if isSafe(board, i, col): 
            # Place this queen in board[i][col] 
            board[i][col] = 1
  
            # recur to place rest of the queens 
            if Deplacer(board, col + 1) == True: 
                return True
  
            # If placing queen in board[i][col 
            # doesn't lead to a solution, then 
            # queen from board[i][col] 
            board[i][col] = 0
  
    # if the queen can not be placed in any row in 
    # this colum col  then return false 
    return False
def solveNQ(): 
    board = [ [0, 0, 0, 0], 
              [0, 0, 0, 0], 
              [0, 0, 0, 0], 
              [0, 0, 0, 0] 
             ] 
  
    if  Deplacer(board, 0) == False: 
        print ("Solution does not exist")
        return False
    else:
        print(board) 
        return True


# In[90]:


Deplacer(board, 0)


# In[91]:


solveNQ()


# In[92]:


def reine(n):
    def _reine(s,n,solutions): 
        if len(s)==n: solutions.append(s)
        else:
            for i1 in set(range(1,n+1))-set(s): 
                liste=[len(s)-j!=abs(i1-i) for j,i in enumerate(s)]
                if not(False in liste): _reine(s+[i1],n,solutions)
    solutions=[]
    _reine([],n,solutions)
    return solutions,('Nombre de solutions : %d' % len(solutions))


# In[93]:


reine(4)


# In[94]:


reine(6)


# In[ ]:




