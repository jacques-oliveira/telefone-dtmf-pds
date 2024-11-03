#%%
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
from scipy.io.wavfile import write

#%%
# Frequências DTMF
dtmf_freqs = {
    '1': (697, 1209),
    '2': (697, 1336),
    '3': (697, 1477),
    '4': (770, 1209),
    '5': (770, 1336),
    '6': (770, 1477),
    '7': (852, 1209),
    '8': (852, 1336),
    '9': (852, 1477),
    '*': (941, 1209),
    '0': (941, 1336),
    '#': (941, 1477)
}

# Função para gerar o sinal DTMF de um dígito
def gerar_tom_dtmf(digit, duration=0.5, sample_rate=8000):
    if digit not in dtmf_freqs:
        raise ValueError("Dígito inválido para DTMF")
    f1, f2 = dtmf_freqs[digit]
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    tone = np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t)
    return tone

# Gerando o sinal para o dígito '5'
sample_rate = 8000
digit = '5'
tone = gerar_tom_dtmf(digit, duration=0.5, sample_rate=sample_rate)

# Salvando o tom como um arquivo de áudio
write("dtmf_5.wav", sample_rate, tone.astype(np.float32))

# Plotando o sinal
plt.plot(tone[:1000])  # Mostrar apenas uma parte do sinal para visualização
plt.title(f"Sinal DTMF para o dígito '{digit}'")
plt.xlabel("Amostras")
plt.ylabel("Amplitude")
plt.show()
