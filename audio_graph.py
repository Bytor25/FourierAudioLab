import matplotlib.pyplot as plt
import numpy as np

def graph_audios_and_frequencies(audios, mix, audio_names):
    plt.figure(figsize=(14, 12))
    

    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'orange', 'purple', 'teal', 'brown']

    for i, audio in enumerate(audios):
        fft_result = np.fft.fft(audio)
        color = colors[i % len(colors)]
        plt.subplot(7, 2, 2*i + 1)
        plt.plot(audio, color=color)
        plt.title(f'Onda de {audio_names[i]}')
        plt.subplot(7, 2, 2*i + 2)
        plt.plot(np.abs(fft_result), color=color)
        plt.title(f'Espectro de Frecuencia de {audio_names[i]}')
    
    fft_mix = np.fft.fft(mix)
    plt.subplot(7, 2, 11)
    plt.plot(mix, color='black')
    plt.title('Onda del Audio Mezclado')
    plt.subplot(7, 2, 12)
    plt.plot(np.abs(fft_mix), color='black')
    plt.title('Espectro de Frecuencia Mezclado')
    plt.tight_layout()
    plt.savefig('audio_analysis.png')
    plt.close()
