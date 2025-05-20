import numpy as np

def normalize(audio):
    max_val = np.max(np.abs(audio))
    if max_val == 0:
        return audio
    return audio / max_val

def delay(audio, rate, delay_time, decay):
    delay_samples = int(delay_time*rate)
    output = np.copy(audio)
    for i in range(delay_samples, len(audio)):
        output[i] += decay*audio[i-delay_samples]
    return normalize(output)

def reverb(audio, rate, delay_time, decay, repeats):
    output = np.copy(audio)
    for r in range(1, repeats):
        delay_samples = int(delay_time * r * rate)
        if delay_samples >= len(audio):
            break
        output[delay_samples:] += (decay ** r) * audio[:-delay_samples]
    return normalize(output)

def chorus(audio, rate, depth, rate_mod):
    output = np.copy(audio)
    mod = (np.sin(2 * np.pi * rate_mod * np.arange(len(audio)) / rate) + 1) / 2
    mod = (mod * depth * rate).astype(int)
    for i in range(len(audio)):
        idx = i - mod[i] if i - mod[i] >= 0 else 0
        output[i] += 0.5 * audio[idx]
    return normalize(output)

def reverse(audio):
    return audio[::-1]

def flanger(audio, rate, max_delay, depth, rate_mod):
    n = len(audio)
    output = np.copy(audio)
    mod = (np.sin(2 * np.pi * rate_mod * np.arange(n) / rate) + 1) / 2
    delay_samples = (mod * max_delay * rate).astype(int)
    for i in range(n):
        idx = i - delay_samples[i]
        if idx >= 0:
            output[i] += depth * audio[idx]
    return normalize(output)

def compressor(audio, threshold, ratio):
    output = np.copy(audio)
    mask = np.abs(audio) > threshold
    output[mask] = np.sign(audio[mask]) * (
        threshold + (np.abs(audio[mask]) - threshold) / ratio
    )
    return normalize(output)

def phaser(audio, rate, depth, rate_mod, stages):
    n = len(audio)
    output = np.copy(audio)
    lfo = (np.sin(2 * np.pi * rate_mod * np.arange(n) / rate) + 1) / 2
    for stage in range(stages):
        y = np.zeros_like(audio)
        fb = depth * lfo
        for i in range(1, n):
            y[i] = -fb[i] * output[i] + output[i-1] + fb[i] * y[i-1]
        output = y
    return normalize(output)

def robot_effect(audio, rate, freq):
    t = np.arange(len(audio)) / rate
    envelope = np.abs(audio)
    carrier = np.sin(2 * np.pi * freq * t)
    robot_audio = envelope * carrier
    return normalize(robot_audio)

def alien_effect(audio, rate, freq):
    t = np.arange(len(audio)) / rate
    modulator = np.sin(2 * np.pi * freq * t)
    alien_audio = audio * modulator
    return normalize(alien_audio)
