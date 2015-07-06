import os
import numpy as np

img_coordinates = input("Enter the image coordinates spaced by comma \ne.g. 1+1j, -1+1j, -1-1j, 1-1j \n")
result = np.fft.fft([img_coordinates])

print(result)