import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


# Tidsverdier og målte temperaturdata
tidspunkt = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60])  # Tidsintervaller i minutter
temperatur_observert = np.array([100, 94, 84, 73, 71, 65, 57, 55, 50, 46, 44, 37, 33, 29, 27, 25, 24, 23.5, 23.9, 23.1, 23])  # Observerte temperaturer i °C

# Konstant verdi for stabil temperatur i omgivelsene
temp_omgivelser = 23  # Stabil omgivelsestemperatur i °C

# Modellering av temperaturendring ved hjelp av eksponentialfunksjon
def modell_temperatur(t, start_temp, nedkjølingsrate):
    return temp_omgivelser + (start_temp - temp_omgivelser) * np.exp(-nedkjølingsrate * t)

# Starttemperaturen ved t=0
start_temp = temperatur_observert[0]

# Tilpass modellparameteren for nedkjølingsrate
optimal_param, _ = curve_fit(lambda t, rate: modell_temperatur(t, start_temp, rate), tidspunkt, temperatur_observert)
nedkjølingsrate = optimal_param[0]

# Beregn forventede temperaturer basert på modellen
modellert_temp = modell_temperatur(tidspunkt, start_temp, nedkjølingsrate)

# Visualisering av data og modell
plt.figure(figsize=(10, 6))
plt.plot(tidspunkt, temperatur_observert, 'o-', label='Observerte data', color='blue')
plt.plot(tidspunkt, modellert_temp, '-', label=f'Teoretisk kurve (rate={nedkjølingsrate:.4f})', color='orange')
plt.xlabel('Tid (minutter)')
plt.ylabel('Temperatur (°C)')
plt.title('Temperaturutvikling: Observerte vs Teoretiske verdier')
plt.legend()
plt.grid(True)
plt.show()

# Utskrift av beregnet nedkjølingsrate
nedkjølingsrate

