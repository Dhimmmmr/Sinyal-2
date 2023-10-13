# -*- coding: utf-8 -*-
def convolution(signal1, signal2):

    result_length = len(signal1) + len(signal2) - 1
    result = [0] * result_length

    for i in range(result_length):
        result[i] = 0
        for j in range(len(signal1)):
            if i - j >= 0 and i - j < len(signal2):
                result[i] += signal1[j] * signal2[i - j]

    return result
print ("Mukhammad Amirul Adhim Ramadhani")
print ("5009211145")

signal1 = [1, 5, 4]
signal2 = [1, 2, 3]
result = convolution(signal1, signal2)

print("Hasil konvolusi:", result)

import numpy as np

numpy_result = np.convolve(signal1, signal2, mode='full')
print("Hasil konvolusi dengan NumPy:", numpy_result)