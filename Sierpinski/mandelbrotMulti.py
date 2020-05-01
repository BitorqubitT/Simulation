# Use python multiprocessing to speed up computation.
# compute_mandelbrot taken from https://github.com/scipy-lectures/scipy-lectures.github.com/blob/master/_downloads/plot_mandelbrot.py

import timeit
from multiprocessing import Pool
import numpy as np
import matplotlib.pyplot as plt
from numpy import newaxis

def compute_mandelbrot(N_max, some_threshold, nx, ny):
    # A grid of c-values
    x = np.linspace(-2, 1, nx)
    y = np.linspace(-1.5, 1.5, ny)

    c = x[:,newaxis] + 1j*y[newaxis,:]

    # Mandelbrot iteration

    z = c
    for j in range(N_max):
        z = z**2 + c

    mandelbrot_set = (abs(z) < some_threshold)

    return mandelbrot_set

def multiprocess(compute, processes):
    pool = Pool(processes=processes)
    results = [pool.apply_async(compute, args=())]
    return results


if __name__ == '__main__':
    aw = multiprocess(compute_mandelbrot(50, 50., 601, 401), 4)
    plt.imshow(aw, extent=[-2, 1, -1.5, 1.5])
    plt.gray()
    plt.show()




