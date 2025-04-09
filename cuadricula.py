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
           
            print("╔" + "═" * (ancho - 2) + "╗")
        elif linea == alto - 1:
           
            print("╚" + "═" * (ancho - 2) + "╝")
        else:
            if linea % 2 == 0:
              
                contenido = Rojo + "#" * (ancho - 2) + blanco
            else:
              
                contenido = verde +  "*" * (ancho - 2) + blanco
           
            print("║" + contenido + "║")


print("Dimensiones del terminal: Contador de  columnas = ", str(dimensiones["col"]).ljust(60), "Contador de  líneas =", str(dimensiones["lines"]).ljust(20))

if __name__ == "__main__":
    dibujar_cuadricula()
print("Registro 1   ")
print("Registro 2   ")
print("Registro 3   ")  

