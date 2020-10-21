import re

while True:
    post = input("voer uw postcode in: ")

    postpatroon = "^[0-9]{4}[A-Z]{2}$"
    postmatches = re.findall(postpatroon, post)

    if(len(postmatches)) > 0:
        break

print("Dank u die post code is in juist formaat: ", postmatches[0])