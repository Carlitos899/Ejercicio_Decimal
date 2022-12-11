numero_binario = input("INGRESA UN BINARIO: ");
numero_decimal = 0 #aquí iremos sumando el resultado de cada multiplicación

for posicion, digito_string in enumerate(numero_binario[::-1]):
	numero_decimal += int(digito_string) * 2 ** posicion

print(f'DECIMAL = {numero_decimal}')

modulos = [] # la lista para guardar los módulos

while numero_decimal != 0: # mientras el número de entrada sea diferente de cero
    # paso 1: dividimos entre 2
    modulo = numero_decimal % 2
    cociente = numero_decimal // 2
    modulos.append(modulo) # guardamos el módulo calculado
    numero_decimal = cociente # el cociente pasa a ser el número de entrada
print(modulos)
	