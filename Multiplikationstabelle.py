# Schreibe kurzes Programm, das eine Multiplikationstabelle für eine vom Benutzer eingegebene Zahl erstellt.
# Das Programm soll die Tabelle von 1 bis 10 anzeigen.

# Benutzer gibt eine Zahl ein
zahl = int(input("Gib eine Zahl ein: "))

# Multiplikationstabelle mit for-Schleife
for i in range(1, 11):  # Schleife von 1 bis 10
    ergebnis = zahl * i
    print(f"{zahl} x {i} = {ergebnis}")