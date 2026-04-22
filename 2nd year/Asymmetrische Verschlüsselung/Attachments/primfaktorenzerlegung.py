import time
from sympy import factorint

# Beispielzahl
zahl = 1234567890123456789

# Zeitmessung starten
startzeit = time.time()

# Primfaktorzerlegung mit sympy
faktoren_dict = factorint(zahl)  # Gibt ein Dictionary {Primzahl: Exponent}
faktoren = []
for prime, exp in faktoren_dict.items():
    faktoren.extend([prime] * exp)

# Zeitmessung beenden
endzeit = time.time()
dauer_ms = (endzeit - startzeit) * 1000

# Ergebnisse ausgeben
print(f"Zahl: {zahl}")
print(f"Primfaktoren: {faktoren}")
print(f"Dauer: {dauer_ms:.2f} ms")
