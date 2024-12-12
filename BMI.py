# Erstellen Sie ein Programm ohne Verzweigung, das den Body-Mass-Index (BMI) berechnet.
# Eine Auswertung(Normalgewicht, Übergewicht, etc.) wird nicht durchgeführt.

print("Bitte das Gewicht in kg eingeben")
Gewicht = float(input())

print("Bitte die Hoehe in cm eingeben")
Hoehe = float(input())

BMI = (Gewicht/((Hoehe/100)**2))

print("Dein BMI beträgt:", BMI)