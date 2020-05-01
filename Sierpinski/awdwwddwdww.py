from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from itertools import product, combinations
from multiprocessing import Pool, TimeoutError
import timeit

def parzen_estimation(x_samples, point_x, h):
    k_n = 0
    for row in x_samples:
        x_i = (point_x - row[:,np.newaxis]) / (h)
        for row in x_i:
            if np.abs(row) > (1/2):
                break
        else: # "completion-else"*
            k_n += 1
    return (h, (k_n / len(x_samples)) / (h**point_x.shape[1]))

def serial(samples, x, widths):
    return [parzen_estimation(samples, x, w) for w in widths]

def multiprocess(processes, samples, x, widths):
    pool = Pool(processes=processes)
    results = [pool.apply_async(parzen_estimation, args=(samples, x, w)) for w in widths]
    results = [p.get() for p in results]
    results.sort() # to sort the results by input window width
    return results

if __name__ == '__main__':

    widths = np.linspace(1.0, 1.2, 100)
    mu_vec = np.array([0,0])
    cov_mat = np.array([[1,0],[0,1]])
    n = 10000

    x_2Dgauss = np.random.multivariate_normal(mu_vec, cov_mat, n)

    benchmarks = []

    benchmarks.append(timeit.Timer('serial(x_2Dgauss, point_x, widths)',
                'from __main__ import serial, x_2Dgauss, point_x, widths').timeit(number=1))

    benchmarks.append(timeit.Timer('multiprocess(2, x_2Dgauss, point_x, widths)',
            'from __main__ import multiprocess, x_2Dgauss, point_x, widths').timeit(number=1))

    benchmarks.append(timeit.Timer('multiprocess(3, x_2Dgauss, point_x, widths)',
            'from __main__ import multiprocess, x_2Dgauss, point_x, widths').timeit(number=1))

    benchmarks.append(timeit.Timer('multiprocess(4, x_2Dgauss, point_x, widths)',
            'from __main__ import multiprocess, x_2Dgauss, point_x, widths').timeit(number=1))

    benchmarks.append(timeit.Timer('multiprocess(6, x_2Dgauss, point_x, widths)',
            'from __main__ import multiprocess, x_2Dgauss, point_x, widths').timeit(number=1))