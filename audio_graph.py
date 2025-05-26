import matplotlib.pyplot as plt
import numpy as np

def graph_audios_and_frequencies_before_after(audios_before, audios_after, mix_before, mix_after, audio_names, filters_used, fs):
    """
    Grafica las ondas y espectros antes y después del filtrado,
    mostrando solo hasta fs/2 Hz en el eje de frecuencia.

    fs: tasa de muestreo (Hz)
    """
    plt.figure(figsize=(16, 15))
    colors_before = ['b', 'g', 'r', 'c', 'm', 'y', 'orange', 'purple', 'teal', 'brown']
    colors_after = ['navy', 'darkgreen', 'maroon', 'teal', 'indigo', 'goldenrod', 'orangered', 'orchid', 'darkslategray', 'peru']

    n_audios = len(audios_before)
    plot_idx = 0
    for i in range(n_audios):
        if audios_before[i] is None or audios_after[i] is None:
            continue
        color_b = colors_before[i % len(colors_before)]
        color_a = colors_after[i % len(colors_after)]
        filtro = filters_used[i] if filters_used and i < len(filters_used) else ""

        # Onda temporal
        plt.subplot(n_audios+1, 2, 2*plot_idx + 1)
        plt.plot(audios_after[i], color=color_a, linestyle='--', label='Después')
        plt.plot(audios_before[i], color=color_b, linestyle='-', label='Antes')
        plt.title(f'Onda de {audio_names[i]} (Filtro: {filtro})')
        plt.legend(loc="upper right")

        # Espectro de frecuencia solo hasta fs/2
        plt.subplot(n_audios+1, 2, 2*plot_idx + 2)
        n = len(audios_before[i])
        freqs = np.fft.rfftfreq(n, d=1/fs)      # Solo frecuencias positivas hasta fs/2
        fft_before = np.fft.rfft(audios_before[i])
        fft_after = np.fft.rfft(audios_after[i])
        plt.plot(freqs, np.abs(fft_after), color=color_a, linestyle='--', label='Después')
        plt.plot(freqs, np.abs(fft_before), color=color_b, linestyle='-', label='Antes')
        plt.xlim([0, fs/2])
        plt.xlabel('Frecuencia (Hz)')
        plt.ylabel('Magnitud')
        plt.title(f'Espectro de Frecuencia de {audio_names[i]} (Filtro: {filtro})')
        plt.legend(loc="upper right")
        plot_idx += 1

    # Mezcla
    if mix_before is not None and mix_after is not None:
        color_mix_b = 'black'
        color_mix_a = 'red'
        plt.subplot(n_audios+1, 2, 2*plot_idx + 1)
        plt.plot(mix_after, color=color_mix_a, linestyle='--', label='Después')
        plt.plot(mix_before, color=color_mix_b, linestyle='-', label='Antes')
        plt.title('Onda del Audio Mezclado')
        plt.legend(loc="upper right")
        plt.subplot(n_audios+1, 2, 2*plot_idx + 2)
        n = len(mix_before)
        freqs = np.fft.rfftfreq(n, d=1/fs)
        fft_mix_before = np.fft.rfft(mix_before)
        fft_mix_after = np.fft.rfft(mix_after)
        plt.plot(freqs, np.abs(fft_mix_after), color=color_mix_a, linestyle='--', label='Después')
        plt.plot(freqs, np.abs(fft_mix_before), color=color_mix_b, linestyle='-', label='Antes')
        plt.xlim([0, fs/2])
        plt.xlabel('Frecuencia (Hz)')
        plt.ylabel('Magnitud')
        plt.title('Espectro de Frecuencia Mezclado')
        plt.legend(loc="upper right")

    plt.tight_layout(rect=[0, 0.03, 1, 0.97])
    plt.suptitle('Colores sólidos: Antes del filtro (arriba) | Colores dashed: Después del filtro (abajo)', fontsize=16)
    plt.savefig('audio_analysis_before_after.png')
    plt.close()