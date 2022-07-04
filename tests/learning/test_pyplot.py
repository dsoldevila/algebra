import pytest
import matplotlib.pyplot as plt
import numpy as np


def test_print_single_vector():
    x_pos = 0
    y_pos = -1
    x_direct = 1
    y_direct = 5
    
    fig, ax = plt.subplots(figsize = (12, 7))
    ax.quiver(x_pos, y_pos, x_direct, y_direct)

    ax.set_title('Quiver plot with one arrow')
    
    plt.show()

def test_print_single_vector_proper_scale():
    x_pos = 0
    y_pos = -1
    x_direct = 1
    y_direct = 5
    
    fig, ax = plt.subplots(figsize = (12, 7))
    ax.quiver(x_pos, y_pos, x_direct, y_direct, scale=1, scale_units='xy', angles='xy')

    ax.set_xlim(-2.0, 2.0)
    ax.set_ylim(-2.0, 6.0)

    ax.set_title('Quiver plot with one arrow')
    
    plt.show()


def test_print_two_vectors():
    x_pos = [0, 1]
    y_pos = [0, 1]
    x_direct = [-1, 1]
    y_direct = [-5, 5]
    
    fig, ax = plt.subplots()

    ax.set_xlim(-2.0, 2.0)
    ax.set_ylim(-2.0, 6.0)

    ax.quiver(x_pos, y_pos, x_direct, y_direct, color=['r', 'b'])
    ax.set_title('Quiver plot with two arrow')
    
    plt.show()




