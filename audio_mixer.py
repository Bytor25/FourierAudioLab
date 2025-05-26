import audio_filters as AF
import filter_audio_config as FAC
import numpy as np
import audio_equalizer_FFT as AEF

def apply_filter(audio, rate, filter_option):
    if filter_option == 1:
        delay_time, decay = FAC.delayConfiguration()
        return AF.delay(audio, rate, delay_time, decay)
    elif filter_option == 2:
        delay_time, decay, repeats = FAC.reverbConfiguration()
        return AF.reverb(audio, rate, delay_time, decay, repeats)
    elif filter_option == 3:
        depth, rate_mod = FAC.chorusConfiguration()
        return AF.chorus(audio, rate, depth, rate_mod)
    elif filter_option == 4:
        return AF.reverse(audio)
    elif filter_option == 5:
        max_delay, depth, rate_mod = FAC.flangerConfiguration()
        return AF.flanger(audio, rate, max_delay, depth, rate_mod)
    elif filter_option == 6:
        depth, rate_mod, stages = FAC.phaserConfiguration()
        return AF.phaser(audio, rate, depth, rate_mod, stages)
    elif filter_option == 7:
        threshold, ratio = FAC.compressorConfiguration()
        return AF.compressor(audio, threshold, ratio)
    elif filter_option == 8:
        freq = FAC.robotEffectConfiguration()
        return AF.robot_effect(audio, rate, freq)
    elif filter_option == 9:
        freq = FAC.alienEffectConfiguration()
        return AF.alien_effect(audio, rate, freq)
    else:
        print("Filtro no implementado, devolviendo audio original.")
        return audio

def mix_audios(audios):
    n = len(audios)
    weights = np.ones(n) / n
    min_length = min(map(len, audios))
    weighted_audios = [a[:min_length] * w for a, w in zip(audios, weights)]
    fft_list = [np.fft.fft(a) for a in weighted_audios]
    mixed_fft = sum(fft_list)
    mixed_audio = np.fft.ifft(mixed_fft).real
    return AF.normalize(mixed_audio)
