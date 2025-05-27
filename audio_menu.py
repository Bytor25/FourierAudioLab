import os

def find_audio_files(root_folder, extensions=('.wav')):
    audio_files = []
    for dirpath, _, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.lower().endswith(extensions):
                audio_files.append(os.path.join(dirpath, filename))
    return audio_files

def select_audios(max_tracks=5):
    audio_files = find_audio_files('sounds')

    if not audio_files:
        print("No se encontraron archivos de audio en la carpeta 'sounds'.")
        return []

    print("\n=== Archivos de audio encontrados ===")
    for idx, filepath in enumerate(audio_files, 1):
        print(f"{idx}: {os.path.relpath(filepath, 'sounds')}")
    print("0: Sin audio") 

    selections = []
    for n in range(max_tracks):
        while True:
            try:
                idx = int(input(f"\nSeleccione el número del audio para el canal #{n+1} (0 para Sin audio): "))
                if idx == 0:
                    selections.extend([None] * (max_tracks - len(selections)))
                    break
                if 1 <= idx <= len(audio_files):
                    selections.append(audio_files[idx - 1])
                    break
                else:
                    print("Opción inválida. Intente de nuevo.")
            except ValueError:
                print("Entrada no válida. Debe ser un número.")
        if len(selections) == max_tracks:
            break

    print("\nArchivos seleccionados:")
    for f in selections:
        print(f if f is not None else "Sin audio")
    return selections