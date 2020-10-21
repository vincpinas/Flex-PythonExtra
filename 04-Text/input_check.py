import re

while True:
    phone = input("voer je mobiele nummer in: ")

    patroon = "^06-?\d{8}$"
    matches = re.findall(patroon, phone)

    if(len(matches)) > 0:
        break

print("Dank u dat nummer is in juiste formaat:", matches[0])
