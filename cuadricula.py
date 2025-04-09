import os
Rojo = "\033[31m"
verde = "\033[32m"
blanco = "\033[37m"

dimensiones = {
    "col": os.get_terminal_size().columns,
    "lines": os.get_terminal_size().lines,
}


def dibujar_cuadricula():
    ancho = dimensiones["col"]
    alto = dimensiones["lines"]

    for linea in range(0,alto):
        if linea == 0:
           
            print(chr(9484) + chr(9472) * (ancho - 2) + chr(9488))
        elif linea == alto - 1:
           
           print(chr(9492) + chr(9472) * (ancho - 2) + chr(9496)) 
        else:
            if linea % 2 == 0:
              
                contenido = Rojo + "#" * (ancho - 2) + blanco
            else:
              
                contenido = verde +  "*" * (ancho - 2) + blanco
           
            print(chr(9474) + contenido + chr(9474)) 


print("Dimensiones del terminal: Contador de  columnas = ", str(dimensiones["col"]).ljust(60), "Contador de  líneas =", str(dimensiones["lines"]).ljust(20))

if __name__ == "__main__":
    dibujar_cuadricula()
numero_registro = 3
for i in range (1,numero_registro +1):
    print("Registro ", str(i).ljust(10))
         

