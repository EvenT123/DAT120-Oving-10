class Flervalgspørsmål:
    def __init__(self, spørsmåltekst, svaralternativ, riktigSvar):
        self.x = spørsmåltekst
        self.y = svaralternativ
        self.z = riktigSvar

    def __str__(self):
        return f"{self.x} \n1: {self.y[0]} \n2: {self.y[1]} \n3: {self.y[2]}"

    def sjekk_svar(self, svar):
        self.f = svar
        if self.f == riktigSvar + 1:
            print("Korrekt!")
        else:
            print("Feil!")


spørsmåltekst = "Hvilke to farger er det svenske flagget?"
svarAlternativ = ["Blå og gul", "Svart og hvit", "Rosa og sølv"]
riktigSvar = 0

x = Flervalgspørsmål(spørsmåltekst, svarAlternativ, riktigSvar)
print(str(x))
brukerSvar = int(input("Hvilket svaralternativ er riktig?: "))
x.sjekk_svar(brukerSvar)