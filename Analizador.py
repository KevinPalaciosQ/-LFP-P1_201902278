objeto = open('carpeta/clase2.ext','r+')

# Imprimir informacion dentro del archivo

# Lee todo el contenido del archivo
print("READ")
print(objeto.read())
# Cerramos el archivo
objeto.close()

objeto = open('carpeta/clase2.ext','r+')
# Lee un caracter de una linea
print("READLINE")
print(objeto.readline(1))
# Cerramos el archivo
objeto.close()

objeto = open('carpeta/clase2.ext','r+')
# Lee todas lineas, linea por linea
print("READLINES")
print(objeto.readlines())
# Cerramos el archivo
objeto.close()

