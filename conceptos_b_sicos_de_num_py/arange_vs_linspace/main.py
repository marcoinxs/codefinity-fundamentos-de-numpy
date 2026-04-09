import numpy as np
# Utilizar la función arange() para crear el arreglo even_numbers.
# Create an array of even numbers from 2 to 21 exclusive
even_numbers = np.arange(2, 21, 2)

# Utilizar la función adecuada para crear el arreglo samples, que permite especificar la cantidad de valores dentro de un intervalo dado.
# Create an array of 10 equally spaced numbers between 5 and 6 exclusive
# Especificar los tres primeros argumentos para crear un arreglo de 10 números equidistantes entre 5 y 6.
# Asegurarse de que 6 no esté incluido en el arreglo samples.
samples = np.linspace(5, 6, 10, endpoint=False)

print(even_numbers)
print(samples)