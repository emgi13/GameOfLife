#Conway's Game of Life

import matplotlib.pyplot as plt
import numpy as np

#Init the Board

nBoardSize = 50 + 2 #2 Borders
Board = np.zeros([nBoardSize,nBoardSize],int)

#Some Initial Shapes

#Blinker
sBlinker = np.array([[0,1,0],[0,1,0],[0,1,0]])

#Shape Loading Func
def LoadShape(b, s, x, y):
    for i in range(s.shape[0]):
        for j in range(s.shape[1]):
            b[x+i+1,y+j+1]=s[i,j]  #Ignoring Borders

#Load a shape
LoadShape(Board, sBlinker, 10, 10)

#Display Image
nFrameNo=0
plt.imshow(Board)
plt.axis("off")
plt.savefig("Images/{:06d}.png".format(nFrameNo), bbox_inches='tight')
plt.close()
