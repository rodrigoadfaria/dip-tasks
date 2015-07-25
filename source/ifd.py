#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import numpy as np
import matplotlib.pyplot as plt


def build_curve_points(descriptors):
    '''
    Draw the points given by the descriptors array in the
    cartesian plane.
    '''
    N=len(descriptors) # size of the descriptors vector
    for x in range(N):
        plt.plot([descriptors[x].real], [descriptors[x].imag], 'ro-', label='python', color='blue')
        
    ylabel = 'Imaginário'.decode('utf8')
    plt.ylabel(ylabel)
    plt.xlabel('Real')

    # limiting the axes to the double of the axes extrema
    boundary = np.amax(plt.axis())
    plt.grid(True, which='both')
    plt.axis((boundary + 1, -boundary - 1, boundary + 1, -boundary - 1))
    
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')

    plt.show()

descriptors = input("Enter the descriptors spaced by comma \ne.g. 1+1j, -1+1j, -1-1j, 1-1j \n")
result = np.fft.ifft([descriptors])

print('The inverse Fourier Transform of ', descriptors, ' is:')
print(result)

build_curve_points(descriptors)