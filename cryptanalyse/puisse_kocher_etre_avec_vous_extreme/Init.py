import numpy as np
import matplotlib.pyplot as plt


plaintexts=np.load('plaintext.npy')
traces=np.load('traces.npy')
ciphertext=np.load('ciphertext.npy')

plt.plot(traces[0])
plt.xlabel("Temps")
plt.ylabel("Consommation")
plt.title("Consommation du matériel pour le début du chiffrement de plaintexts[0]")
plt.show()




