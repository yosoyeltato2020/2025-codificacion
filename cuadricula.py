import os


dimensiones = {
    "col": os.get_terminal_size().columns,
    "lines": os.get_terminal_size().lines,
}


def dibujar_cuadricula():
    ancho = dimensiones["col"]
    alto = dimensiones["lines"]

    for linea in range(alto):
        if linea == 0:
           
            print("╔" + "═" * (ancho - 2) + "╗")
        elif linea == alto - 1:
           
            print("╚" + "═" * (ancho - 2) + "╝")
        else:
            if linea % 2 == 0:
              
                contenido = "#" * (ancho - 2)
            else:
              
                contenido = "*" * (ancho - 2)
           
            print("║" + contenido + "║")


print(f" Contador de las dimensiones del terminal: Contador de las = {dimensiones['col']}, contador de las líneas = {dimensiones['lines']}")
dibujar_cuadricula()
