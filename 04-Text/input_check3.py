import re

while True:
    kenteken = input("voer uw kenten in: ")

    kentekenpatroon = "^[A-Z]{2}-123-[A-Z]{3}$"
    kentekenmatches = re.findall(kentekenpatroon, kenteken)

    if(len(kentekenmatches)) > 0:
        break

print("Dank u dat kenteken nummer is in juist formaat: ", kentekenmatches[0])