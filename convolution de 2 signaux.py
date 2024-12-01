import numpy as np
import matplotlib.pyplot as plt
def convolution(x, y):

    len_x = len(x)
    len_y = len(y)
    
    
    output_size = len_x+len_y - 1
    h = np.zeros(output_size)
    

    for i in range(len_x):
        for j in range(len_y):
            h[i + j] += x[i] * y[j]
    
    return h

x = [-1, 2,3]
y = [0, 1, 0,5]

# Calcul de la convolution
resultat = convolution(x, y)

# Affichage des résultats
print("x:", x)
print("y:", y)
print("Convolution :", resultat)

np_result = np.convolve(x, y, mode='full')
print("Convolution :", np_result)
resultat = convolution(x, y)

np_result = np.convolve(x, y, mode='full')


plt.figure(figsize=(20, 15))

# Signal x
plt.subplot(3, 1, 1)
plt.stem(range(len(x)), x, linefmt='b-', markerfmt='bo', basefmt='r-')
plt.title("Signal x")
plt.xlabel("Temps")
plt.ylabel("Amplitude")

# Signal y
plt.subplot(3, 1, 2)
plt.stem(range(len(y)), y, linefmt='g-', markerfmt='go', basefmt='r-')
plt.title("Signal y")
plt.xlabel("Temps")
plt.ylabel("Amplitude")

# Convolution h
plt.subplot(3, 1, 3)
plt.stem(range(len(resultat)), resultat, linefmt='m-', markerfmt='mo', basefmt='r-')
plt.title("Convolution des deux signaux")
plt.xlabel("Temps")
plt.ylabel("Amplitude")
plt.tight_layout()
plt.show()
