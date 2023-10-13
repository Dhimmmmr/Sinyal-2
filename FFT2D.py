import numpy as np
import matplotlib.pyplot as plt

def fft2d(x):
    M, N = x.shape
    if M <= 1 and N <= 1:
        return x
    else:
        # FFT dalam arah kolom
        for i in range(M):
            x[i, :] = np.fft.fft(x[i, :])
        
        # FFT dalam arah baris
        for j in range(N):
            x[:, j] = np.fft.fft(x[:, j])
        
        return x

def generate_2d_signal(M, N, A, width):
    t = np.outer(np.linspace(-width * A, width * A, M), np.ones(N))
    signal = np.where((t >= -width * A) & (t <= width * A), 1, 0)
    return signal

def plot_2d_signal_and_fft(signal, title):
    output = fft2d(signal)
    output_oneside = np.abs(output)[:M // 2, :N // 2]

    plt.figure(figsize=(12, 6))
    
    plt.subplot(1, 2, 1)
    plt.imshow(signal, cmap='gray', extent=(-width * A, width * A, -width * A, width * A))
    plt.title(title + ' Signal')
    
    plt.subplot(1, 2, 2)
    plt.imshow(np.log(1 + output_oneside), cmap='gray', extent=(0, width * A, 0, width * A))
    plt.title('2D FFT of ' + title)

    plt.show()

A = 2
width = 1.0
M = N = 128

signal1 = generate_2d_signal(M, N, A, width)
signal2 = generate_2d_signal(M, N, A, 2 * width)
signal3 = generate_2d_signal(M, N, A, 3 * width)

plot_2d_signal_and_fft(signal1, 'Signal 1 (A)')
plot_2d_signal_and_fft(signal2, 'Signal 2 (2A)')
plot_2d_signal_and_fft(signal3, 'Signal 3 (3A)')

