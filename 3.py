import os
print(os.path.abspath("out.csv"))


import numpy as np
arr_rand = np.array([8, 8, 3, 7, 7, 0, 4, 2, 5, 2])
print("Arreglo: ", arr_rand)

# Obtener índices (posiciones) en los que el valor sea > 5
indices_mayores_5 = np.where(arr_rand > 5)
print("Posiciones en donde el valor > 5:", indices_mayores_5)

arr_rand.take(indices_mayores_5)

arr_rand[indices_mayores_5]

print("Posición del elemento más grande (max):", np.argmax(arr_rand))
print("Posición del elemento más chico (min):", np.argmin(arr_rand))

np.set_printoptions(suppress=True)
ruta_url = 'https://raw.githubusercontent.com/selva86/datasets/master/Auto.csv'
data = np.genfromtxt(ruta_url, delimiter=',', skip_header=1, filling_values=-999, dtype='float')
data[:3]

data2 = np.genfromtxt(ruta_url, delimiter=',', skip_header=1, dtype=None, encoding=None)
data2[:3]

data3 = np.genfromtxt(ruta_url, delimiter=',', skip_header=1, dtype=float, filling_values=-999)
data3[:3]

np.savetxt("out.csv", data3, delimiter=",")
