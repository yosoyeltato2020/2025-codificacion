import os

# Print the size of terminal

dimensiones = {
    "col": os.get_terminal_size().columns,
    "lines": os.get_terminal_size().lines,
}

print(dimensiones)
