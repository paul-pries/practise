gender = input("Bitte gib dein Geschlecht: m/w:\n ")
if gender == "m" or gender == "w":
    print("Tippe dein Gewicht in Kg ein: ")
    weight = float(input())
    print("Tippe deine Größe in Meter ein: ")
    height = float(input())
    # Berechnung
    BMI = float(weight)/((float(height))**2)
    print("Dein BMI beträgt: ", BMI)

    if gender == "m" and BMI < 20 or gender == "w" and BMI < 19:
        print("Du bist untergewichtig.")
    elif gender == "m" and BMI >= 20 and BMI < 25 or gender == "w" and BMI >= 19 and BMI < 24:
        print("Du bist normalgewichtig.")
    elif gender == "m" and BMI >= 25 and BMI < 30 or gender == "w" and BMI >= 24 and BMI < 30:
        print("Du bist übergewichtig.")
    elif gender == "m" and BMI >= 30 and BMI <= 40 or gender == "w" and BMI >= 30 and BMI <= 40:
        print("Du bist adipös.")
    elif gender == "m" and BMI > 40 or gender == "w" and BMI > 40:
        print("Du bist massiv adipös.")
else:
    print("Bitte gib das Geschlecht in folgendem Format ein: m oder w.")