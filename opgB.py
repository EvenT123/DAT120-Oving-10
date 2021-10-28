class Flervalgspørsmål: #Oppretter klassen flervalgspørsmål
    def __init__(self, spørsmåltekst, svaralternativ, riktigSvar):
        self.x = spørsmåltekst #Spørsmålteksten
        self.y = svaralternativ #Svaralternativene
        self.z = riktigSvar #Det riktige svaret

    def __str__(self): #__str__ metode som returnerer en streng
        return f"{self.x} \n1: {self.y[0]} \n2: {self.y[1]} \n3: {self.y[2]}" #Skriver ut spørsmålstekst og svaralternativ

    def sjekk_svar(self, svar): #Funksjon for å sjekke om svaret er korrekt
        self.f = svar #Brukeren sitt svar
        if self.f == riktigSvar + 1: #+1 for å matche riktigSvar med nummeret på svaralternativet
            print("Korrekt!")
        else:
            print("Feil!")

#Spørsmålstekst, svaralternativ og riktig svar til spørsmålet
spørsmåltekst = "Hvilke to farger er det svenske flagget?"
svarAlternativ = ["Blå og gul", "Svart og hvit", "Rosa og sølv"] #Liste med svaralternativ
riktigSvar = 0 #Indexen til det riktige svaret i listen

#Oppretter objektet x med klassen Flervalgspørsmål() med parametere tilpasset spørsmålet
x = Flervalgspørsmål(spørsmåltekst, svarAlternativ, riktigSvar)
print(str(x)) #Printer ut spørsmålstekst og svaralternativ
brukerSvar = int(input("Hvilket svaralternativ er riktig?: ")) #Input hvor brukeren svarer på spørsmålet
x.sjekk_svar(brukerSvar) #Utfører funksjonen sjekk_svar() for å sjekke om svaret er riktig