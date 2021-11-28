import random

from Simulacion import Simulacion


def obtener_dimensiones_entorno():
    num_filas_y_columnas = 0
    while True:
        print("¿Quiere establecer dimensiones de entorno? Introduzca 's'(sí) o 'n'(no)")
        decision = input()
        if decision == "s" or decision == "S":
            print("Introduzca el número de filas y columnas del entorno de la sabana")
            print("NOTA: Es un solo parámetro, ya que la matriz del entorno es cuadrada")
            print("NOTA: La matriz como mínimo tiene que ser 5x5")
            try:
                num_filas_y_columnas = int(input())
            except ValueError:
                print("ERROR: El número de filas y columnas pasado no es entero. Vuelva a intentarlo")
        elif decision == "n" or decision == "N":
            num_filas_y_columnas = 75
        else:
            print("ERROR: Tiene que introducir la letra 's' (sí) o 'n' (no) para tomar una decisión")
        if num_filas_y_columnas >= 5:
            break
        elif num_filas_y_columnas < 5 and num_filas_y_columnas != 0:
            print("ERROR: El número de filas y columnas es menor que 5")
    return num_filas_y_columnas


def obtener_num_individuos():
    num_leones = num_hienas = num_cebras = 0
    while True:
        print("¿Quiere introducir el número de animales del entorno? Introduzca 's'(sí) o 'n'(no)")
        print(
            "NOTA: Por cada león deben haber como mínimo 3 hienas (relación 1:3) y 6 cebras ("
            "relacion 1:6)")
        print(
            "NOTA: Como mínimo deben haber 2 manadas de cada especie, es decir, deben haber mínimamente 2 "
            "leones")
        decision = input()
        if decision == "s" or decision == "S":
            try:
                print("Introduzca el número de leones del entorno de la sabana")
                num_leones = int(input())
                print("Introduzca el número de hienas del entorno de la sabana")
                num_hienas = int(input())
                print("Introduzca el número de cebras del entorno de la sabana")
                num_cebras = int(input())
            except ValueError:
                print("ERROR: El número de individuos de alguna especie no es entero. Vuelva a intentarlo")
        elif decision == "n" or decision == "N":
            num_leones = random.randint(2, 575)
            num_hienas = random.randint(num_leones * 3, num_leones * 3 + 100)
            num_cebras = random.randint(num_leones * 6, num_leones * 6 + 100)
        else:
            print("ERROR: Tiene que introducir la letra 's' (sí) o 'n' (no) para tomar una decisión")
        if (num_leones >= 2 and num_hienas >= 3 * num_leones
                and num_cebras >= 6 * num_leones):
            break
        else:
            print("La correspondencia entre número de individuos es incorrecta. Vuelva a intentarlo")
    return num_cebras, num_hienas, num_leones


def obtener_num_manadas(num_cebras, num_hienas, num_leones):
    if num_leones == 2 or num_leones == 3:
        num_manadas_leones = 2
    else:
        num_manadas_leones = random.randint(2, int(num_leones / 2))
    num_manadas_hienas = random.randint(2, int(num_hienas / 2))
    num_manadas_cebras = random.randint(2, int(num_cebras / 2))
    return num_manadas_cebras, num_manadas_hienas, num_manadas_leones


def main():
    dimensiones = obtener_dimensiones_entorno()
    num_cebras, num_hienas, num_leones = obtener_num_individuos()
    num_manadas_cebras, num_manadas_hienas, num_manadas_leones = obtener_num_manadas(num_cebras, num_hienas, num_leones)
    simulacion = Simulacion()
    simulacion.iniciar_entorno(dimensiones)
    print(simulacion.entorno)
    simulacion.iniciar_animales(num_leones, num_hienas, num_cebras, num_manadas_leones, num_manadas_hienas, num_manadas_cebras)
    simulacion.lanzar_simulacion()


if __name__ == "__main__":
    main()
