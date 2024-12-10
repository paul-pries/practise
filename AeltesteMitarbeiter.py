print("Willkommen zum Mitarbeiter Management Programm (MMP)\n"
      "====================================================\n"
      "Bislang kann ich berechnen, wer der älteste Mitarbeiter ist.\n"
      "Bitte gib mir folgende Angaben..")
m1_name = input("Namen des ersten Mitarbeiters: ")
m1_alter = int(input("Alter des ersten Mitarbeiters: "))
m2_name = input("Namen des zweiten Mitarbeiters: ")
m2_alter = int(input("Alter des zweiten Mitarbeiters: "))
m3_name = input("Namen des dritten Mitarbeiters: ")
m3_alter = int(input("Alter des dritten Mitarbeiters: "))
m4_name = input("Namen des vierten Mitarbeiters: ")
m4_alter = int(input("Alter des vierten Mitarbeiters: "))
#Vergleich
if m1_alter > m2_alter and m1_alter > m3_alter and m1_alter > m4_alter:
    oldest = m1_name
    oldest_age = m1_alter
elif m2_alter > m1_alter and m2_alter > m3_alter and m2_alter > m4_alter:
    oldest = m2_name
    oldest_age = m2_alter
elif m3_alter > m1_alter and m3_alter > m2_alter and m3_alter > m4_alter:
    oldest = m3_name
    oldest_age = m3_alter
elif m4_alter>m1_alter and m4_alter>m2_alter and m4_alter>m3_alter:
    oldest = m4_name
    oldest_age = m4_alter
#Output
print("Der älteste Mitarbeiter ist:", oldest, "und er/sie ist", oldest_age, "Jahre alt!\n"
    "======================== ENDE =========================")