# Transformada de Fourier
<p align="center">
  <img src="https://github.com/user-attachments/assets/6d5c66ef-b346-4df4-9e33-dadadabd0de2" height="140"/>
</p>

## Contextualização:

Quando você liga para uma empresa com atendimento automático, é comum ouvir a
frase: "Para falar com o setor X, disque 3". Isso acontece porque o sistema reconhece
o que você digita no telefone pela frequência sonora gerada pelos números. 
Esse processo é possível graças ao DTMF. DTMF (Dual Tone Multi Frequency) é o som
que ouvimos ao pressionar os dígitos no teclado dotelefone. Esses sons são compostos por dois tons
distintos, cada um com uma frequência diferente (uma para cada número), o que explica o nome Dual-Tone
Multi Frequency, traduzido como "dois tons, múltiplas frequências". Assim, ao digitar
um número no seu dispositivo durante o atendimento, o sistema capta a frequência sonora correspondente
à tecla e interpreta o comando que deve ser executado (Fonte:Nvoip).

<p align="center">
  <img src="https://github.com/user-attachments/assets/e9b9649a-c5bd-4781-a39b-55103cceadb2" alt="Screenshot de DTMF">
</p>


# Objetivo:

Desenvolver um programa em Python que simule um telefone, gere o som
DTMF correspondente a um número de telefone, aplique a FFT no sinal para identificar
as frequências dominantes e, a partir da análise da FFT, decodifique e identifique o
dígito.
