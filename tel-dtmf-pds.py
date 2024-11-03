#%%
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
from scipy.io.wavfile import write

#%%
# Frequências DTMF usando par chave valor
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
#%%
# Função para gerar o sinal DTMF de um dígito
#que usa o conceito de superposição
def gerar_tom_dtmf(digit, duration=0.5, sample_rate=8000):
    if digit not in dtmf_freqs:
        raise ValueError("Dígito inválido para DTMF")
    f1, f2 = dtmf_freqs[digit]
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    tone = np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t)
    return tone

# Gerando o sinal para o dígito '5'
digitoTest = '4'
tone = gerar_tom_dtmf(digitoTest)

#%%
# Salvando o tom como um arquivo de áudio
def salvar_tom_audio(digito):
    nomeArquivo = "dtmf_" + str(digito) +".wav"
    write(nomeArquivo, 8000,tone.astype(np.float32))

salvar_tom_audio(digitoTest)

#%%
# Plotando o sinal
def plot_sinal(digito,partSinal=1000):
    plt.plot(tone[:partSinal])  # Mostrar apenas uma parte do sinal para visualização
    plt.title(f"Sinal DTMF para o dígito '{digito}'")
    plt.xlabel("Amostras")
    plt.ylabel("Amplitude")
    plt.show()

plot_sinal(digitoTest)
#%%
#Função para plotar as frequências atráves da fft
def plot_fft(signal, sample_rate=8000):
    N = len(signal)
    yf = fft(signal)
    xf = fftfreq(N, 1 / sample_rate)
    
    # Apenas frequências positivas
    idxs = np.where(xf > 0)
    xf = xf[idxs]
    yf = np.abs(yf[idxs])

    plt.plot(xf, yf)
    plt.title("Espectro de Frequências do Sinal DTMF")
    plt.xlabel("Frequência (Hz)")
    plt.ylabel("Amplitude")
    plt.show()

#Plotando as frequências encontradas    
plot_fft(tone)

#%%
def detecta_digito_dtmf(signal, sample_rate=8000):
    N = len(signal)
    yf = fft(signal)
    xf = fftfreq(N, 1 / sample_rate)

    # Filtrar frequências positivas
    idxs = np.where(xf > 0)
    xf = xf[idxs]
    yf = np.abs(yf[idxs])

    # Identificar as duas frequências mais fortes
    peaks = np.argsort(yf)[-2:]
    detected_freqs = xf[peaks]
    detected_freqs.sort()

    # Mapeamento das frequências para o dígito DTMF
    for digit, (f1, f2) in dtmf_freqs.items():
        if np.isclose(detected_freqs[0], f1, atol=10) and np.isclose(detected_freqs[1], f2, atol=10):
            return digit
    return None

# Testando a detecção do dígito
detected_digit = detecta_digito_dtmf(tone)
print(f"Dígito detectado: {detected_digit}")

