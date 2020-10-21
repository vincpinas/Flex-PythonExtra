import re

emails = []

with open("tekstmetemails.txt", "r") as bestand:

    regel = bestand.readline()
   
    while regel:
        # Vul de juiste regular expression voor een email in op de puntjes
        patroon = r"[\w\.-]+@[\w\.-]+"

        # Gebruik de juiste code op de plaats van de puntjes
        gevonden = re.findall(patroon, regel)

        # Alle gevonden emails aan de email list toevoegen
        emails.extend(gevonden)
        
        # Volgende regel lezen
        regel = bestand.readline()

for l in emails:
    print(l)


lengte = len(emails)
i = 0

with open("uidaging1.txt", "w") as f:
    while i < lengte:
        f.write(emails[i])
        f.write("\n")
        i += 1