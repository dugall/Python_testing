import numpy as np
x = np.array([[ 1,  2,  3,  4],
              [ 5,  6,  7,  8],
              [ 9, 10, 11, 12]])

# reshaping an array
print (x.reshape(3, 2, 2))
#array([[[ 1,  2],
#        [ 3,  4]],
#
#       [[ 5,  6],
#        [ 7,  8]],
#
#       [[ 9, 10],
#        [11, 12]]])

# Transposing an array: reversing
# the ordering of its axes. This interchanges
# the rows and columns of `x`
print (x.transpose())
#array([[ 1,  5,  9],
#       [ 2,  6, 10],
#       [ 3,  7, 11],
#       [ 4,  8, 12]])