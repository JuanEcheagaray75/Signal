import numpy as np


def closest_power_of_two(n):
    count = 0

    # First n in the below
    # condition is for the
    # case where n is 0
    if (n and not(n & (n - 1))):
        return n

    while(n != 0):
        n >>= 1
        count += 1

    return 1 << count


# Implementación vectorizada que hace uso de Numpy, mucho más eficiente y veloz
def fft_v(x):

    # Converting to numpy array (for efficiency purposes, we intend to use Numba later on)
    # Get the length of the array
    x = np.asarray(x, dtype=float)
    N = x.shape[0]

    # Check if the length of x is a power of 2, if not, pad with zeros at the end of it
    if np.log2(N) % 1 > 0:
        N = closest_power_of_two(N)
        # Pad with zeros at the end of x
        x = np.pad(x, (0, N - len(x)), 'constant', constant_values=(0))

    # Checks if N is smaller than 2, if so, an error will be raised
    # There is no need to perform an FFT on a single point
    N_min = min(N, 2)

    n = np.arange(N_min)
    k = n[:, None]
    M = np.exp(-2j * np.pi * n * k / N_min)
    X = np.dot(M, x.reshape((N_min, -1)))

    while X.shape[0] < N:
        X_even = X[:, :int(X.shape[1] / 2)]
        X_odd = X[:, int(X.shape[1] / 2):]
        terms = np.exp(-1j * np.pi * np.arange(X.shape[0])
                       / X.shape[0])[:, None]
        X = np.vstack([X_even + terms * X_odd,
                       X_even - terms * X_odd])

    return X.ravel()


# Classic recursive implementation designed upon Cooley-Tukey's fft algorithm idea
# The implementation presented above is a vectorized version of this implementation 
# that runs much faster using Numpy's vector operations
def FFT(x):
    N = len(x)

    if N == 1:
        return x
    else:
        # Apply FFT to odd and even terms, independently
        X_even = FFT(x[::2])
        X_odd = FFT(x[1::2])

        factor = np.exp(-2j * np.pi * np.arange(N) / N)

        # Now we just add up all the factors we obtained
        X = np.concatenate([X_even + factor[:int(N/2)] * X_odd, X_even + factor[int(N/2):] * X_odd])
        return X
