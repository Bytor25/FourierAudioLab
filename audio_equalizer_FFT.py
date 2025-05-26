import numpy as np

def equalize_fft(audio, rate, gains_db):
    N = len(audio)
    fft_audio = np.fft.fft(audio)
    freqs = np.fft.fftfreq(N, 1/rate)
    band_edges = np.logspace(np.log10(20), np.log10(rate//2), len(gains_db)+1)
    gains = 10**(np.array(gains_db)/20.0)
    for i in range(len(gains)):
        mask = (np.abs(freqs) >= band_edges[i]) & (np.abs(freqs) < band_edges[i+1])
        fft_audio[mask] *= gains[i]
    eq_audio = np.fft.ifft(fft_audio).real
    max_abs = np.max(np.abs(eq_audio))
    if max_abs > 0:
        eq_audio /= max_abs
    return eq_audio