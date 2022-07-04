import pytest
import matplotlib.pyplot as plt
import numpy as np




def test_print_vectors():
    V = np.array([[1,1], [-2,2], [4,-7]])
    origin = np.array([[0, 0, 0],[0, 0, 0]]) # origin point

    plt.quiver(*origin, V[:,0], V[:,1], color=['r','b','g'], scale=21)
    plt.show()




