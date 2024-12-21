# Jugendliche sind nach deutschem Recht Menschen im Alter zwischen 14 und 18 Jahren.
# Schreibe ein Programm, das den Benutzer nach dem Alter fragt und dann entscheidet, ob er oder sie ein Jugendlicher ist oder nicht.

alter = int(input("Wie alt sind Sie?\n "))
if alter<=18 and alter >=14:
    print("Glückwunsch, Sie sind ein Jugendlicher")
else:
    print("Sie sind kein Jugendlicher")