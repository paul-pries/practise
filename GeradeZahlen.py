# Schreibe ein Programm, das prüft, ob eine eingegebene Zahl gerade oder ungerade ist.

# Benutzer nach einer Zahl fragen
zahl = int(input("Bitte gib eine Zahl ein: "))

# Überprüfen, ob die Zahl gerade oder ungerade ist
if zahl % 2 == 0:
    print("Die Zahl ist gerade.")
else:
    print("Die Zahl ist ungerade.")

# Optional: Überprüfen, ob die Zahl negativ ist
if zahl < 0:
    print("Die Zahl ist negativ.")