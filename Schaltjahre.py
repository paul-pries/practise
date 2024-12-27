# Im Jahre 1582 wurde von Papst Gregor XII. eine Kalenderreform angeordnet, die auch heute noch gültig ist.
# Darin wurde festgelegt, welche Kalenderjahre 366 statt 365 Tage haben sollen.
# Diese Jahre nennt man seitdem Schaltjahre. In Schaltjahren hat der Februar 29 anstatt 28 Tage. Die Regel lautet folgendermaßen:
# Ein Jahr ist ein Schaltjahr, wenn die Jahreszahl entweder ohne Rest durch 400 teilbar ist oder wenn die Jahreszahl ohne Rest durch 4 und gelichzeitig nicht durch 100 teilbar ist.
# Zum Beispiel sind die Jahre 2000 und 2004 Schaltjahre, nicht aber 2003 oder 1900.

jahr = int(input("Bitte geben Sie das aktuelle Jahr ein! \n "))
if jahr % 400 == 0 or (jahr % 4 == 0 and jahr % 100 != 0):
    print ("Glückwunsch, es handelt sich beim eingegebenen Jahr um ein Schaltjahr")
else:
    print ("Das Jahr", jahr, "ist kein Schaltjahr.")