#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import numpy as np
import matplotlib.pyplot as plt

descriptors = input("Enter the descriptors spaced by comma \ne.g. 1+1j, -1+1j, -1-1j, 1-1j \n")
result = np.fft.ifft([descriptors])

print('The inverse Fourier Transform of ', descriptors, ' is:')
print(result)

N=len(descriptors) # size of the descriptors vector
for x in range(N):
    plt.plot([descriptors[x].real], [descriptors[x].imag], 'ro-', label='python')
    
ylabel = 'Imaginário'.decode('utf8')
plt.ylabel(ylabel)
plt.xlabel('Real')
plt.show()