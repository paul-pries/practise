dogyear = int(input("Gib das Alter deines Hundes ein:\n"))
if dogyear < 1:
    print("Das Alter muss mindestens 1 Jahr Alt sein.")
elif dogyear <= 2:
    alter = dogyear*7
    print("Das Alter des Hundes beträgt",alter,"Jahre in Menschenjahre." )
elif dogyear >=3:
    secondalter = 2*7 + (dogyear-2)*5
print("Das Alter des Hundes beträgt",secondalter,"Jahre in Menschenjahren")