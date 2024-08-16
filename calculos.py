import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

R = 2200  
C = 0.0000022
eletromotriz = 11  


def calcular_corrente(t, R, C, eletromotriz):
    return (eletromotriz / R) * np.exp(-t / (R * C))


def calcular_voltagens(t, R, C, eletromotriz):
    V_R = eletromotriz * np.exp(-t / (R * C))
    V_C = eletromotriz * (1 - np.exp(-t / (R * C)))
    return V_R, V_C

tempos = np.arange(0, 6, 0.5)
correntes = calcular_corrente(tempos * 1e-3, R, C, eletromotriz)  
voltagens_R_C = np.array([calcular_voltagens(t * 1e-3, R, C, eletromotriz) for t in tempos])
voltagens_R = voltagens_R_C[:, 0]
voltagens_C = voltagens_R_C[:, 1]


dados = {
    "Tempo (ms)": tempos,
    "Corrente (mA)": correntes * 1e3,
    "Voltagem no Resistor (V)": voltagens_R,
    "Voltagem no Capacitor (V)": voltagens_C
}
df = pd.DataFrame(dados)


fig, ax = plt.subplots(figsize=(10, 2))  
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')


plt.savefig("tabela_resultados.pdf", dpi=300, bbox_inches='tight')
plt.show()


plt.figure(figsize=(10, 6))
plt.plot(tempos, correntes * 1e3, marker='o', label='Corrente (mA)')
plt.title('Corrente no Circuito RC ao Longo do Tempo')
plt.xlabel('Tempo (ms)')
plt.ylabel('Corrente (mA)')
plt.grid(True)
plt.legend()
plt.savefig("corrente_circuito.pdf")  
plt.show()


plt.figure(figsize=(10, 6))
plt.plot(tempos, voltagens_R, marker='o', label='Voltagem no Resistor (V)')
plt.plot(tempos, voltagens_C, marker='o', label='Voltagem no Capacitor (V)')
plt.title('Voltagens no Resistor e no Capacitor ao Longo do Tempo')
plt.xlabel('Tempo (ms)')
plt.ylabel('Voltagem (V)')
plt.grid(True)
plt.legend()
plt.savefig("voltagens_circuito.pdf")  
plt.show()
