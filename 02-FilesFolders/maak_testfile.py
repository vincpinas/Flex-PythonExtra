import io

bestand = open("klasgenoten.txt", "w")

bestand.write("Test 123!");

bestand.close()

bestand2 = open("klasgenoten.txt", "r")

bestand2.write("Lekker alles overschrijven")
