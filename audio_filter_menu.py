def get_available_filters():
    return {
        0: "Sin filtro",
        1: "Delay",
        2: "Reverb",
        3: "Chorus",
        4: "Reverse",
        5: "Flanger",
        6: "Phaser",
        7: "Compressor",
        8: "Robot filter",
        9: "Alien filter"
    }

def select_filters(audio_files):
    available_filters = get_available_filters()
    print("\n=== Opciones de filtro disponibles ===")
    for key, val in available_filters.items():
        print(f"{key}: {val}")

    selections = []
    for idx, file in enumerate(audio_files):
        print(f"\nAudio {idx + 1}: {file}")
        for key, val in available_filters.items():
            print(f"  {key}: {val}")
        while True:
            try:
                selected = int(input(f"Seleccione el filtro para '{file}' (número): "))
                if selected in available_filters:
                    selections.append(selected)
                    break
                else:
                    print("Opción inválida.")
            except:
                print("Ingrese un número válido.")
    return selections