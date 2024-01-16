"""
Lsn32-Linear Systems
Jacob Hildebrand
3/23/23
Solve linear systems
"""

import numpy as np

#define
# A = np.array([[5,2],[4,-3]])
# b = np.array([8,1])
A = np.array([[3,-2,1],[4,0,-6],[1,3,-2]])
b = np.array([5,1,9])

if np.linalg.det(A) ==0:
    print('\nThe A matrix is singular so')
    print('the system cannot be solved\n')
else:
    x = np.linalg.solve(A,b)



    #print
    print(f'\nA Matrix\n{A}')
    print(f'\nb Vector\n{b}')
    print()
    for i in range(len(x)):
        print(f'x{i+1} = {x[i]:.3f}')
    print()