numero_decimal = input("INGRESA UN VALOR: "); # este es el número que queremos convertir a binario
numero_decimal = (int(numero_decimal));

modulos = [] # la lista para guardar los módulos
print("¿Cómo se llama?");
nombre = input();
print(f"Me alegro de conocerle, {nombre}");
    
while numero_decimal != 0: # mientras el número de entrada sea diferente de cero
    # paso 1: dividimos entre 2
    modulo = numero_decimal % 2
    cociente = numero_decimal // 2
    modulos.append(modulo) # guardamos el módulo calculado
    numero_decimal = cociente # el cociente pasa a ser el número de entrada
print(modulos)