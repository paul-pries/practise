# Variable für die Gesamtsumme initialisieren
gesamtsumme = 0

print("Gib positive Zahlen ein, um sie zu summieren. Gib 0 ein, um zu beenden.")

# while-Schleife starten
while True:
    # Benutzer nach einer Zahl fragen
    zahl = int(input("Gib eine Zahl ein (0 zum Beenden): "))

    # Beenden der Schleife, wenn 0 eingegeben wird
    if zahl == 0:
        break

    # Nur positive Zahlen zur Gesamtsumme hinzufügen
    if zahl > 0:
        gesamtsumme += zahl

# Gesamtsumme ausgeben
print(f"Die Gesamtsumme der positiven Zahlen ist: {gesamtsumme}")