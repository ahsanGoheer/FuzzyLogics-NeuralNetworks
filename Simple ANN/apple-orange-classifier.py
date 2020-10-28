import numpy as np


def sym_hard_limit(x):
    if x<0:
        return -1
    elif x>=0:
        return 1

if __name__ == "__main__":

      orange=np.array([1,-1,-1],ndmin=2).T
      apple=np.array([1,1,-1],ndmin=2).T
      weights = np.array([0,1,0])

      y=np.dot(weights,apple)+0
      a=sym_hard_limit(y)
      if a==1:
          print('apple')
      else:
          print('orange')
    
       