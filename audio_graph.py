import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks

def graph_audios_and_frequencies_after(audios_after, mix_after, audio_names, filters_used, fs):
    plt.figure(figsize=(18, 15))
    colors_after = ['navy', 'darkgreen', 'maroon', 'teal', 'indigo', 'goldenrod', 'orangered', 'orchid', 'darkslategray', 'peru']

    n_audios = len(audios_after)
    plot_idx = 0
    for i in range(n_audios):
        if audios_after[i] is None:
            continue
        color_a = colors_after[i % len(colors_after)]
        filtro = filters_used[i] if filters_used and i < len(filters_used) else ""

        # Onda temporal
        plt.subplot(n_audios+1, 3, 3*plot_idx + 1)
        n = len(audios_after[i])
        tiempo = np.linspace(0, n/fs, n)
        plt.plot(tiempo, audios_after[i], color=color_a, linestyle='--', label='Después')
        plt.xlabel('Tiempo (s)')
        plt.title(f'Onda de {audio_names[i]} (Después del filtro: {filtro})')
        plt.legend(loc="upper right")

        # Espectro de frecuencia
        plt.subplot(n_audios+1, 3, 3*plot_idx + 2)
        freqs = np.fft.rfftfreq(n, d=1/fs)
        fft_after = np.abs(np.fft.rfft(audios_after[i]))
        plt.plot(freqs, fft_after, color=color_a, linestyle='--', label='Después')

        # Pico más relevante
        peaks, _ = find_peaks(fft_after, height=np.max(fft_after)*0.1)
        if len(peaks) > 0:
            max_peak_idx = peaks[np.argmax(fft_after[peaks])]
            freq = freqs[max_peak_idx]
            amp = fft_after[max_peak_idx]
            plt.annotate(f'{freq:.1f}Hz\n{amp:.1f}',
                         (freq, amp),
                         textcoords="offset points",
                         xytext=(0, 10),
                         ha='center',
                         fontsize=8,
                         color=color_a)
        else:
            freq, amp = 0, 0

        plt.xlim([0, fs/2])
        plt.xlabel('Frecuencia (Hz)')
        plt.ylabel('Magnitud')
        plt.title(f'Espectro de Frecuencia de {audio_names[i]}')
        plt.legend(loc="upper right")

        # Tabla a la derecha
        plt.subplot(n_audios+1, 3, 3*plot_idx + 3)
        table_data = [['Frecuencia (Hz)', f'{freq:.2f}'], ['Amplitud', f'{amp:.2f}']]
        plt.axis('off')
        plt.table(cellText=table_data, colWidths=[0.3, 0.3], cellLoc='center', loc='center')
        plt.title('Pico más relevante', fontsize=10)

        plot_idx += 1

    # Audio mezclado
    if mix_after is not None:
        color_mix_a = 'red'
        plt.subplot(n_audios+1, 3, 3*plot_idx + 1)
        n = len(mix_after)
        tiempo = np.linspace(0, n/fs, n)
        plt.plot(tiempo, mix_after, color=color_mix_a, linestyle='--', label='Después')
        plt.xlabel('Tiempo (s)')
        plt.title('Onda del Audio Mezclado (Después)')
        plt.legend(loc="upper right")

        plt.subplot(n_audios+1, 3, 3*plot_idx + 2)
        freqs = np.fft.rfftfreq(n, d=1/fs)
        fft_mix_after = np.abs(np.fft.rfft(mix_after))
        plt.plot(freqs, fft_mix_after, color=color_mix_a, linestyle='--', label='Después')

        peaks, _ = find_peaks(fft_mix_after, height=np.max(fft_mix_after)*0.1)
        if len(peaks) > 0:
            max_peak_idx = peaks[np.argmax(fft_mix_after[peaks])]
            freq = freqs[max_peak_idx]
            amp = fft_mix_after[max_peak_idx]
            plt.annotate(f'{freq:.1f}Hz\n{amp:.1f}',
                         (freq, amp),
                         textcoords="offset points",
                         xytext=(0, 10),
                         ha='center',
                         fontsize=8,
                         color=color_mix_a)
        else:
            freq, amp = 0, 0

        plt.xlim([0, fs/2])
        plt.xlabel('Frecuencia (Hz)')
        plt.ylabel('Magnitud')
        plt.title('Espectro de Frecuencia Mezclado (Después)')
        plt.legend(loc="upper right")

        plt.subplot(n_audios+1, 3, 3*plot_idx + 3)
        table_data = [['Frecuencia (Hz)', f'{freq:.2f}'], ['Amplitud', f'{amp:.2f}']]
        plt.axis('off')
        plt.table(cellText=table_data, colWidths=[0.3, 0.3], cellLoc='center', loc='center')
        plt.title('Pico más relevante', fontsize=10)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.suptitle('Análisis de Audios (Solo después del filtrado)', fontsize=16)
    plt.savefig('audio_analysis_after_only.png')
    plt.close()
