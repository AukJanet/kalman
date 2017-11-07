
import numpy as np
from numpy.linalg import inv
from numpy import dot

x = np.array([[0.], [0.]]) # initial state (location and velocity)
P = np.array([[1000., 0.], 
              [0., 1000.]]) # initial uncertainty
u = np.array([[0.], [0.]])         # external motion
F = np.array([[1., 1.], [0, 1.]])  # next state function
H = np.array([[1., 0.]])           # measurement function
R = np.array([[1]])               # Measurement uncertainty
I = np.array([[1., 0.], [0., 1.]]) # identity matrix


measurements = [1.52839861735, 2.09456834295, 0.65717830838, 
                3.54006128603, 3.37541657732, 3.86522255384, 
                6.36519844993, 9.82167712014, 8.51246308423, 
                9.08639862688, 10.5965587495, 11.4618312646, 
                12.8216294204, 12.6860280302, 15.662376304, 
                16.1647795555, 14.5342812343, 17.4949856103, 
                18.9682697028, 20.2619859403, ]

# actuals = [0, 1, 2, 3, 4, 5, 6, 
#           7, 8, 9, 10, 11, 12, 
#           13, 14, 15, 16, 17, 18, 19]


def kalman_filter(x, P):
    for n in range(len(measurements)):
        # Measurement Update
        # -- fill in here --

        # example for K
        # K = dot(dot(P, np.transpose(H)), inv(S))
        

        # Prediction
        # -- fill in here --

        # print position and velocity
        print "x=", x[0][0], "v=", x[1][0] 
    return x, P

print kalman_filter(x, P)


# output should be:
# x: [[~20], [~1]]

        
