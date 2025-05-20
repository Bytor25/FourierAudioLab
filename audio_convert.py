def ensure_mono(audio):
    if len(audio.shape) > 1:
        return audio.mean(axis=1)
    return audio