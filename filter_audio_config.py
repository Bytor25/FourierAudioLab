def delayConfiguration():
    print("Opciones de Delay:")
    print("1. Eco suave")
    print("2. Efecto ligero")
    print("3. Efecto tipo catedral o montaña")

    try:
        option = int(input("Seleccione una opción: "))
    except ValueError:
        print("Entrada inválida. Se usará la opción 1 por defecto.")
        option = 1

    if option == 1:
        return 0.3, 0.5
    elif option == 2:
        return 0.1, 0.3
    elif option == 3:
        return 0.7, 0.8
    else:
        print("Opción no válida. Se usará la opción 1 por defecto.")
        return 0.3, 0.5


def reverbConfiguration():
    print("Opciones de Reverb:")
    print("1. Ambiente pequeño")
    print("2. Sala mediana")
    print("3. Caverna o iglesia")

    try:
        option = int(input("Seleccione una opción: "))
    except ValueError:
        print("Entrada inválida. Se usará la opción 1 por defecto.")
        option = 1

    if option == 1:
        return 0.05, 0.4, 3
    elif option == 2:
        return 0.08, 0.6, 5
    elif option == 3:
        return 0.12, 0.8, 7
    else:
        print("Opción no válida. Se usará la opción 1 por defecto.")
        return 0.05, 0.4, 3


def chorusConfiguration():
    print("Opciones de Chorus:")
    print("1. Suave")
    print("2. Moderado")
    print("3. Intenso")

    try:
        option = int(input("Seleccione una opción: "))
    except ValueError:
        print("Entrada inválida. Se usará la opción 1 por defecto.")
        option = 1

    if option == 1:
        return 0.0015, 1.2
    elif option == 2:
        return 0.002, 1.5
    elif option == 3:
        return 0.003, 2.0
    else:
        print("Opción no válida. Se usará la opción 1 por defecto.")
        return 0.0015, 1.2


def flangerConfiguration():
    print("Opciones de Flanger:")
    print("1. Sutil")
    print("2. Clásico")
    print("3. Profundo")

    try:
        option = int(input("Seleccione una opción: "))
    except ValueError:
        print("Entrada inválida. Se usará la opción 1 por defecto.")
        option = 1

    if option == 1:
        return 0.002, 0.5, 0.2
    elif option == 2:
        return 0.003, 0.7, 0.25
    elif option == 3:
        return 0.005, 1.0, 0.3
    else:
        print("Opción no válida. Se usará la opción 1 por defecto.")
        return 0.002, 0.5, 0.2


def compressorConfiguration():
    print("Opciones de Compresor:")
    print("1. Suave")
    print("2. Moderado")
    print("3. Fuerte")

    try:
        option = int(input("Seleccione una opción: "))
    except ValueError:
        print("Entrada inválida. Se usará la opción 1 por defecto.")
        option = 1

    if option == 1:
        return 0.7, 2.0
    elif option == 2:
        return 0.6, 4.0
    elif option == 3:
        return 0.5, 8.0
    else:
        print("Opción no válida. Se usará la opción 1 por defecto.")
        return 0.7, 2.0


def phaserConfiguration():
    print("Opciones de Phaser:")
    print("1. Ligero")
    print("2. Medio")
    print("3. Intenso")

    try:
        option = int(input("Seleccione una opción: "))
    except ValueError:
        print("Entrada inválida. Se usará la opción 1 por defecto.")
        option = 1

    if option == 1:
        return 0.5, 0.3, 3
    elif option == 2:
        return 0.7, 0.4, 4
    elif option == 3:
        return 1.0, 0.6, 5
    else:
        print("Opción no válida. Se usará la opción 1 por defecto.")
        return 0.5, 0.3, 3


def alienEffectConfiguration():
    print("Opciones de Efecto Alien:")
    print("1. Baja frecuencia")
    print("2. Frecuencia media")
    print("3. Alta frecuencia")

    try:
        option = int(input("Seleccione una opción: "))
    except ValueError:
        print("Entrada inválida. Se usará la opción 1 por defecto.")
        option = 1

    frecuencias = {1: 60, 2: 80, 3: 120}
    if option not in frecuencias:
        print("Opción no válida. Se usará la opción 1 por defecto.")
        option = 1
    return frecuencias[option]

def robotEffectConfiguration():
    print("Opciones para efecto Robot:")
    print("1. Frecuencia baja")
    print("2. Frecuencia media")
    print("3. Frecuencia alta")

    try:
        option = int(input("Seleccione una opción: "))
    except ValueError:
        print("Entrada inválida. Se usará la opción 1 por defecto.")
        option = 1

    if option == 1:
        return 50
    elif option == 2:
        return 100
    elif option == 3:
        return 150
    else:
        print("Opción no válida. Se usará la opción 1 por defecto.")
        return 50
