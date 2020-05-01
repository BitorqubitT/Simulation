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

mandelbrot_set = compute_mandelbrot(50, 50., 601, 401)

plt.imshow(mandelbrot_set.T, extent=[-2, 1, -1.5, 1.5])
plt.gray()
plt.show()




# zet al die verschillende manieren in 1 bestand ???
#gebruik die code van ibm en implement multithreading?????
#Zou dit ook kunnen in python.
#Google tpu gebruiken????




"""from pylab import *
from numpy import NaN
 
def m(a):
	z = 0
	for n in range(1, 100):
		z = z**2 + a
		if abs(z) > 2:
			return n
	return NaN
 
X = arange(-2, .5, .002)
Y = arange(-1,  1, .002)
Z = zeros((len(Y), len(X)))
 
for iy, y in enumerate(Y):
	print (iy, "of", len(Y))
	for ix, x in enumerate(X):
		Z[iy,ix] = m(x + 1j * y)
 
imshow(Z, cmap = plt.cm.prism, interpolation = 'none', extent = (X.min(), X.max(), Y.min(), Y.max()))
xlabel("Re(c)")
ylabel("Im(c)")
savefig("mandelbrot_python.svg")
show()"""