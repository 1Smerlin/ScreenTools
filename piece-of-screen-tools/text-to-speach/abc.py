allLetras = "abcdefghijklmnopqrstuvwxyzäöüßABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜ"
allKlein = "abcdefghijklmnopqrstuvwxyzäöüß"
allGroß = "ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜ"
abcKlein = "abcdefghijklmnopqrstuvwxyz"
abcGroß = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
spezialKlein = "äöüß"
spezialGroß = "ÄÖÜ"
selbstKlein = "aeiouäöü"
selbstGroß = "AEIOUÄÖÜ"
mitlauteKlein = "bcdfghjklmnpqrstvwxyzß"
mitlauteGroß = "BCDFGHJKLMNPQRSTVWXYZ"

space = "\n"
umbruch = "\n"
print(mitlauteKlein[0])
with open("laute.txt", "w") as file:
    for j in selbstKlein:
        print(j)
        file.write(j+space)
    file.write(j+umbruch)
    for i in mitlauteGroß:
        for j in selbstKlein:
            print(i+j)
            file.write(i+j+space)
        file.write(i+j+umbruch)
    for j in selbstKlein:
        print("sch"+j)
        file.write("sch"+j+space)
    file.write("sch"+j+umbruch)
