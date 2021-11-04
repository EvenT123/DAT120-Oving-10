class Sporsmaal: #Oppretter klassen flervalgspørsmål
    def __init__(self, sporsmaaltekst, svaralternativ, riktigSvar):
        self.x = sporsmaaltekst #Spørsmålteksten
        self.y = svaralternativ #Det riktige svaret
        self.z = riktigSvar #Svaralternativene
        

    def __str__(self): #__str__ metode som returnerer en streng
        return f"{self.x} {self.y} {self.z}" #Skriver ut spørsmålstekst og svaralternativ
    
    def korrekt_svar_tekst(self):
        
        
        return

liste = []
with open("sporsmaalsfil.txt", "r", encoding="UTF8") as fil1:
    for linje in fil1:
        spmEnd = linje.find(":")
        spm = linje[:spmEnd]
        
        rsStart = spmEnd + 2
        rsEnd = linje.find(":", rsStart)
        rs = int(linje[rsStart:rsEnd])
        
        saStart = linje.find(":", rsEnd) + 1
        sa = linje[saStart:]
        
        x = Sporsmaal(spm, rs, sa)
        liste.append(str(x))

print(liste)
