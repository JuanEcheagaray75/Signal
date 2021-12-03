# from pre_processing import *
from fourier_transform import *
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')


def main():
    # Ciclar por todos los archivos de prueba que se nos dieron
    for csv_file in os.listdir("data\\test_data"):

        # Lectura del archivo
        print("Leyendo archivo: " + csv_file)
        df = pd.read_csv("data\\test_data\\" + csv_file, header=None).T
        df['Amplitude'] = df[0] + df[1]
        df.pop(0)
        df.pop(1)

        # Aplicar transformada de Fourier
        print("Aplicando transformada de Fourier")
        yfft = fft_v(df['Amplitude'])

        # Plot the resulting Fourier transform,
        # feel free to modify the frequency domain used
        print("Generando gráfico")
        xf = np.linspace(0, 20000, len(yfft))
        # No te asustes, la transformada de Fourier
        # (al aplicarle el valor absoluto) genera un gráfico simétrico
        plt.plot(xf, np.abs(yfft))
        plt.xlabel("k")
        plt.ylabel("|Y(k)|")
        filename = csv_file.split(".")[0]
        plt.title("Transformada de Fourier de " + filename)
        plt.savefig("images\\" + filename + ".eps", format='eps')
        plt.close()
        

print("Iniciando programa")
main()
print("Programa terminado")
