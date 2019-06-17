#Conway's Game of Life

import matplotlib.pyplot as plt
import numpy as np

#Init the Board

nBoardSize = 75 + 2 #2 Borders
Board = np.zeros([nBoardSize,nBoardSize],int)
nFrames = 100

#Shape Definer
def DefineShape(sFileName):
    return np.array([[1 if i=='#' else 0 for i in j.strip()] for j in open(sFileName,'r').read().strip().split('\n')])



#Some Initial Shapes

#Blinker
sSpaceShip = DefineShape("Shapes/SpaceShip.txt")

#Shape Loading Func
def LoadShape(b, s, x, y):
    for i in range(s.shape[0]):
        for j in range(s.shape[1]):
            b[x+i+1,y+j+1]=s[i,j]  #Ignoring Borders

#Update Board
def Update(b):
    b2 = np.copy(b)
    nbrs=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    for i in range(1,b.shape[0]-1):
        for j in range(1,b.shape[1]-1):
            s=0
            for k in nbrs:
                s+=b[i+k[0],j+k[1]]
            birth = (b[i,j]==0 and s==3)
            alive = b[i,j]==1 and (s==2 or s==3)
            b2[i,j] = 1 if (birth or alive) else 0
    return b2

#Load a shape
LoadShape(Board, sSpaceShip, 10, 10)

#Display Image
nFrameNo=0
plt.imshow(Board)
plt.axis("off")
plt.savefig("Images/{:06d}.png".format(nFrameNo), bbox_inches='tight')
plt.close()

#Animation Loop
while(nFrameNo<nFrames):
    nFrameNo+=1
    print(nFrameNo)
    Board=Update(Board)
    plt.imshow(Board)
    plt.axis("off")
    plt.savefig("Images/{:06d}.png".format(nFrameNo), bbox_inches='tight')
    plt.close()
