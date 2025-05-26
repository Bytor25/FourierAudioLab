import os

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
    filters = []
    print("\n=== Filtros disponibles ===")
    for idx in sorted(available_filters):
        print(f"{idx}: {available_filters[idx]}")

    for i, file in enumerate(audio_files):
        if file is None:
            filters.append(0)
            continue
        base_name = os.path.basename(file)
        print(f"\nSelecciona un filtro para '{base_name}':")
        while True:
            try:
                choice = int(input("Ingresa el número del filtro: "))
                if choice in available_filters:
                    filters.append(choice)
                    print(f"Seleccionado: {available_filters[choice]}")
                    break
                else:
                    print("Opción no válida. Intente de nuevo.")
            except ValueError:
                print("Por favor ingresa un número válido.")
    return filters