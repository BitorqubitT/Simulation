#Generate mandelbrot with JIT.
# compute_mandelbrot taken from https://github.com/scipy-lectures/scipy-lectures.github.com/blob/master/_downloads/plot_mandelbrot.py

import matplotlib.pyplot as plt
import numpy as np
from numpy import newaxis
from numba import jit
import timeit





tic = timeit.default_timer()
@jit
def compute_mandelbrot(N_max, some_threshold, nx, ny):
    # Create array between x,y value , n indicates the amount of numbers.
    x = np.linspace(-2, 1, nx)
    y = np.linspace(-1.5, 1.5, ny)

    # create a complex expression. (python uses J for imaginary)
    c = x[:, newaxis] + 1j * y[newaxis, :]

    # Mandelbrot iteration

    # We can skip z = 0 ??????
    z = c
    for j in range(N_max):
        z = z ** 2 + c

    mandelbrot_set = (abs(z) < some_threshold)

    return mandelbrot_set


# waarom gebruiken we 50. ?????

mandelbrot_set = compute_mandelbrot(10050, 50., 100, 300)

#plt.imshow takes in an array structure.
plt.imshow(mandelbrot_set.T, extent=[-2, 1, -1.5, 1.5])
plt.gray()
plt.show()

toc = timeit.default_timer()
print(toc - tic)
