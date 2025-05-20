import soundfile as sf
import audio_convert as AC
import audio_filter_menu as AFM
import audio_mixer as MX
import audio_graph as AG
import os
import folder_managenment as FM
import audio_menu as AM


FM.folder_existence('filtered_audios')
FM.folder_existence('output_audio')

FM.clear_folder('filtered_audios')

audio_files = AM.select_audios()

audios = []
audio_names = []

rate = None
for file in audio_files:
    if file is None:
        continue 
    audio, sr = sf.read(file)
    audio = AC.ensure_mono(audio)
    if rate is None:
        rate = sr
    audios.append(audio)

    base_name = os.path.splitext(os.path.basename(file))[0]
    audio_names.append(base_name)

# Seleccionar filtros para cada audio
filters = AFM.select_filters(audio_files)


# Aplicar filtros, guardar cada audio filtrado, y construir la lista para mezclar
filtered_audios = []
for audio_file, audio, filter_idx in zip(audio_files, audios, filters):
    if audio_file is None:
        continue 
    filtered_audio = MX.apply_filter(audio, rate, filter_idx)
    filtered_audios.append(filtered_audio)
    filter_name = AFM.get_available_filters()[filter_idx].replace(" ", "_").lower()
    base_name = os.path.splitext(os.path.basename(audio_file))[0]
    output_name = f"{base_name}_{filter_name}.wav"
    output_path = os.path.join("filtered_audios", output_name)
    sf.write(output_path, filtered_audio, rate)
    print(f"Guardado: {output_path}")

# Mezclar los audios filtrados
mixed_audio = MX.mix_audios(filtered_audios)
sf.write('output_audio/mixed_audio.wav', mixed_audio, rate)

# Graficar resultados
AG.graph_audios_and_frequencies(filtered_audios, mixed_audio, audio_names)
print("Listo. Archivo mezclado y gráficas guardadas.")