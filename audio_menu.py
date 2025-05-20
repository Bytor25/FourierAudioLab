def get_available_audios():
    return {
        1: "Feid",
        2: "Michael jackson",
        3: "Diomedez diaz",
        4: "Reggaeton",
        5: "vallenato",
        6: "Percusión",
        7: "Bajo",
        8: "Guitarra electrica",
        9: "Sin audio"
    }

def select_audios():
    audio_files = [
        'sounds/vocals/feid.wav',
        'sounds/vocals/michael.wav',
        'sounds/vocals/diomedez.wav',
        'sounds/melody/spot.wav',
        'sounds/melody/vallenato.wav',
        'sounds/instruments/01_Drums.wav',
        'sounds/instruments/02_Bass.wav',
        'sounds/instruments/03_Electric_Left.wav'
    ]

    available_audios = get_available_audios()
    print("\n=== Opciones de audio disponibles ===")
    for key, val in available_audios.items():
        print(f"{key}: {val}")

    selections = []
    while len(selections) < 5:
        try:
            idx = int(input(f"\nSeleccione el número del audio #{len(selections)+1}: "))
            if idx < 1 or idx > 9:
                print("Opción inválida. Intente de nuevo.")
                continue
            if idx in selections:
                print("Ya seleccionó este audio. Elija otro.")
                continue
            selections.append(idx)
        except ValueError:
            print("Entrada no válida. Debe ser un número.")

    selected_files = []
    for idx in selections:
        if idx == 9:
            selected_files.append(None)
        else:
            selected_files.append(audio_files[idx - 1])

    print("\nArchivos seleccionados:")
    for f in selected_files:
        print(f)
    return selected_files