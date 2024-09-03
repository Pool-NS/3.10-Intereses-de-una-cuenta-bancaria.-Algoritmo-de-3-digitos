# Lee tres números del usuario
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))

# Crea una lista con los números
numeros = [num1, num2, num3]

# Ordena la lista en orden ascendente
numeros.sort()

# Imprime los números ordenados
print("Los números en orden ascendente son:")
for numero in numeros:
    print(numero)
