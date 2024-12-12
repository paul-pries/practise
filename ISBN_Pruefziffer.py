# Die ISBN besteht aus 10 Ziffern.

# z1 z2 z3 z4 z5 z6 z7 z8 z9 z10
# Die letzte Ziffer z10 ist eine Prüfziffer. Sie berechnet sich wie folgt:

# Zuerst wird eine Art Quersumme nach folgender Formel gebildet:

# s    =    1*z1 + 2*z2 +  3*z3  + 4*z4  + 5*z5  + 6*z6  +  7*z7  + 8*z8  + 9*z9

# Die Prüfziffer z10 ist der Rest der ganzzahligen Division von s durch 11, also  s % 11.


# Beispiel: Für die ISBN 3826604237 lautet die Prüfziffer 7
# Rechnung:    1*3+2*8+3*2+4*6+5*6+6*0+7*4+8*2+9*3    =    150

# Der Rest der Division von 150 durch 11 ist 7. (Die Ganzzahldivision von 150 durch 11 hat das Ergebnis 13 hat. 11 mal 13 ergibt 143.
# Es bleiben als 7 bis zur 150 über. Also ergibt 150 % 11 = 7.)

# Schreiben Sie ein Programm, das die Prüfziffer einer ISBN berechnet. Eingegeben wird eine
# neunstellige natürliche Zahl. Ausgegeben wird die Prüfziffer als Zahl zwischen 0 und 10.

isbn = input ("Bitte die ISBN eingeben: ")

quersumme = 1*int(isbn[0])+2*int(isbn[1])+3*3*int(isbn[2])+4*int(isbn[3])+5*int(isbn[4])+6*int(isbn[5])+7*int(isbn[6])+8*int(isbn[7])+9*int(isbn[8])
pruefziffer = quersumme%11

print("Die Prüfziffer lautet: ", pruefziffer)