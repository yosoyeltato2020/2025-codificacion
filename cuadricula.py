import os


VERDE = "\033[32m"
AMARILLO = "\033[33m"
AZUL = "\033[34m"
CIAN = "\033[36m"
RESET = "\033[0m"


dimensiones = {
    "col": os.get_terminal_size().columns,
    "lines": os.get_terminal_size().lines,
}


def dibujar_cuadricula_con_ascii():
    ancho = dimensiones["col"]
    alto = dimensiones["lines"]

    for linea in range(alto):
        if linea == 0:
           
            print(CIAN + "╔" + "═" * (ancho - 2) + "╗" + RESET)
        elif linea == alto - 1:
           
            print(CIAN + "╚" + "═" * (ancho - 2) + "╝" + RESET)
        else:
            if linea % 2 == 0:
              
                contenido = AMARILLO + "*" * (ancho - 2) + RESET
            else:
              
                contenido = " " * (ancho - 2)
           
            print(CIAN + "║" + RESET + contenido + CIAN + "║" + RESET)


print(VERDE + f"Dimensiones del terminal: columnas = {dimensiones['col']}, líneas = {dimensiones['lines']}" + RESET)
dibujar_cuadricula_con_ascii()
