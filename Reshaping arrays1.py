import numpy as np

# construct a new random number generator
rng = np.random.default_rng()

# create a shape-(3,3) array by drawing its entries randomly
# from the uniform distribution [0, 1)
rng.random((3, 3))
np.array([[ 0.09542611,  0.13183498,  0.39836068],
       [ 0.7358235 ,  0.77640024,  0.74913595],
       [ 0.37702688,  0.86617624,  0.39846429]])

# create a shape-(5,) array by drawing its entries randomly
# from a mean-0, variance-1 normal (a.k.a. Gaussian) distribution
rng.normal(size=(5,))
np.array([-1.11262121, -0.35392007,  0.4245215 , -0.81995588,  0.65412323])
