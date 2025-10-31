"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    with open("files/input/data.csv", "r") as file:
        letter_sums = {}
        for line in file:
            parts = line.split("\t")
            letter = parts[0]
            col5_values = map(int, parts[4].split(","))
            total_col5 = sum(col5_values)
            if letter in letter_sums:
                letter_sums[letter] += total_col5
            else:
                letter_sums[letter] = total_col5
    return dict(sorted(letter_sums.items()))
