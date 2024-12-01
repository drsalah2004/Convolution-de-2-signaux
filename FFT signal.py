import numpy as np
import matplotlib.pyplot as plt

Fs = 1000  # sampling frequency(Hz)
T = 1      # Durée (s)
t = np.linspace(0, T, int(Fs*T), endpoint=False)  # Axe temporel
f1 , f2 , f3 = 50 , 120 , 180 # sine frequency (Hz)
x = np.cos(2 * np.pi * f1 * t) + 5 * np.cos(2 * np.pi * f2 * t)+np.cos(np.pi* f3 * t)

# Calcul de la FFT
fft_result = np.fft.fft(x)
fft_frequency = np.fft.fftfreq(len(x), 1/Fs)  # Fréquences associées

# Magnitude (uniquement la partie positive du spectre)
positive_freqs = fft_frequency[:len(fft_frequency)//2]
partie_positive = np.abs(fft_result[:len(fft_result)//2])

plt.figure(figsize=(12, 6))

# Signal temporel
plt.subplot(2, 1, 1)
plt.plot(t, x)
plt.title("Signal temporel de x")
plt.xlabel("Temps (s)")
plt.ylabel("Amplitude")

# Spectre de fréquence
plt.subplot(2, 1, 2)
plt.plot(positive_freqs, partie_positive)
plt.title("Spectre de fréquence (FFT)")
plt.xlabel("Fréquence (Hz)")
plt.ylabel("Amplitude")
plt.tight_layout()
plt.show()



                       #Filtre numérique FIR (filtre passe bas LPF)
from scipy.signal import firwin, lfilter


cutoff = 100  # Fréquence de coupure (Hz)
numtaps = 1000  # Nombre de coefficients du filtre
fir_coeff = firwin(numtaps, cutoff, fs=Fs, pass_zero='lowpass')


x_filtre = lfilter(fir_coeff, 1.0, x)
plt.figure(figsize=(10, 4))
plt.plot(t, x, label="Signal original")
plt.plot(t, x_filtre, label="Signal filtré (FIR)")
plt.title("Filtrage FIR passe-bas")
plt.xlabel("Temps (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.show()

                     #Filtre numérique IIR (Infinite Impulse Response)                       

 
from scipy.signal import butter, filtfilt

# Conception d'un filtre IIR passe-bas
order = 4  # Ordre du filtre
cutoff_iir = 100  # Fréquence de coupure (Hz)
b , a = butter(order, cutoff_iir / (Fs / 2), btype='low')  

# Filtrage du signal
filtered_x_iir = filtfilt(b, a, x)

# Affichage du signal filtré
plt.figure(figsize=(10, 4))
plt.plot(t, x, label="Signal original")
plt.plot(t, filtered_x_iir, label="Signal filtré (IIR)")
plt.title("Filtrage IIR passe-bas")
plt.xlabel("Temps (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.show()
