import soundfile as sf
import audio_convert as AC
import audio_filter_menu as AFM
import audio_mixer as MX
import audio_graph as AG
import os
import folder_managenment as FM
import audio_menu as AM
import audio_equalizer_FFT as AEQ  # Importa tu ecualizador FFT

gains_db = [3, 2, 1, 0, -1, -1, 0, 1, 2, 3]

FM.folder_existence('filtered_audios')
FM.folder_existence('output_audio')
FM.clear_folder('filtered_audios')

audio_files = AM.select_audios()

audios = []
audio_names = []
rate = None

for file in audio_files:
    if file is None:
        audios.append(None)
        audio_names.append("Sin audio")
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

# Obtener nombres de filtros para cada audio
filter_names = []
available_filters = AFM.get_available_filters()
for idx, file in enumerate(audio_files):
    if file is None:
        filter_names.append("Sin filtro")
    else:
        filter_names.append(available_filters[filters[idx]])

# Aplicar filtros y ecualizador, guardar cada audio filtrado y ecualizado, construir la lista para mezclar
filtered_audios = []
for audio_file, audio, filter_idx in zip(audio_files, audios, filters):
    if audio_file is None or audio is None:
        filtered_audios.append(None)
        continue 
    # Aplica el filtro seleccionado
    filtered_audio = MX.apply_filter(audio, rate, filter_idx)
    # Aplica el ecualizador FFT de 10 bandas
    filtered_audio = AEQ.equalize_fft(filtered_audio, rate, gains_db)
    filtered_audios.append(filtered_audio)
    filter_name = AFM.get_available_filters()[filter_idx].replace(" ", "_").lower()
    base_name = os.path.splitext(os.path.basename(audio_file))[0]
    output_name = f"{base_name}_{filter_name}_eq.wav"
    output_path = os.path.join("filtered_audios", output_name)
    sf.write(output_path, filtered_audio, rate)
    print(f"Guardado: {output_path}")

# Mezclar los audios originales y filtrados/ecualizados (sin None)
audios_valid = [a for a in audios if a is not None]
filtered_valid = [a for a in filtered_audios if a is not None]

mixed_audio_before = MX.mix_audios(audios_valid) if audios_valid else None
mixed_audio_after = MX.mix_audios(filtered_valid) if filtered_valid else None

if mixed_audio_after is not None:
    sf.write('output_audio/mixed_audio.wav', mixed_audio_after, rate)

# Graficar resultados incluyendo los nombres de los filtros usados
AG.graph_audios_and_frequencies_before_after(
    audios_before=audios,
    audios_after=filtered_audios,
    mix_before=mixed_audio_before,
    mix_after=mixed_audio_after,
    audio_names=audio_names,
    filters_used=filter_names,
    fs=rate  
)

print("Listo. Archivo mezclado y gráficas guardadas.")