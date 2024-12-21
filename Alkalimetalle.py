# Alkalimetalle sind die Stoffe Litium (Li), Natrium (Na), Kalium(K), Rubidium(Rb) und Ceasium(Cs).
# Schreibe ein Programm, das Folgendes leistet: Der Benutzer gibt die Formel eines chemischen Elementes an.
# Anschließend wird gemeldet, ob es sich um ein Alkalimetall handelt oder nicht.

metalle = input("Bitte geben Sie die Formel eines chemischen Elements ein! \n ")
if metalle == "Li" or metalle == "Na" or metalle == "K" or metalle == "Rb" or metalle == "Cs":
    print("Glückwunsch, es handelt sich um ein Metall")
else:
    print("Das ist leider kein Metall")