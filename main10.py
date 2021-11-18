class Sporsmaal: #Oppretter klassen flervalgspørsmål
    def __init__(self, sporsmaaltekst, svaralternativ, riktigSvar):
        self.x = sporsmaaltekst #Spørsmålteksten
        self.y = svaralternativ #Det riktige svaret
        self.z = riktigSvar #Svaralternativene
        

    def __str__(self): #__str__ metode som returnerer en streng
        string = ""
        index = 0
        string += f"\n{self.x}\nSvaralternativer:\n" #Skriver ut spørsmålstekst og "svaralternativ:"   
        for i in saListe:
            alt = saListe[index]
            string += f"{index}: {alt}\n"
            index += 1
        return string #Returnerer stringen
    
    def korrekt_svar_tekst(self): #Metode som returerer teksten for riktig svaralternativ
        return f"\nKorrekt svar: {saListe[rs]}"
    
class Spiller: #Oppretter klassen spiller
    def __init__(self, navn, poengsum):
        self.x = navn 
        self.y = poengsum

liste = []
saListe = []
spiller1Poeng = 0
spiller2Poeng = 0
with open("sporsmaalsfil.txt", "r", encoding="UTF8") as fil1:
    for linje in fil1:
        spmEnd = linje.find(":")
        spm = linje[:spmEnd]
        
        rsStart = spmEnd + 2
        rsEnd = linje.find(":", rsStart)
        rs = int(linje[rsStart:rsEnd])
        
        saStart = linje.find(":", rsEnd) + 2
        sa = linje[saStart:]
        z = 0
        saListe = []
        for tegn in sa:
            saEnd = sa.find(",", z) + 1
            if saEnd == 0:
               saEnd = len(sa) - 2
               saListe.append(sa[z + 1:saEnd])
               break
            saListe.append(sa[z + 1:saEnd - 1])
            z = saEnd
            
        x = Sporsmaal(spm, sa, rs)
        
        if __name__=="__main__":
            print(str(x))
            spiller1Svar = int(input("Velg et svaralternativ for spiller 1: "))
            spiller2Svar = int(input("Velg et svaralternativ for spiller 2: "))
            print(x.korrekt_svar_tekst())
            
            if spiller1Svar == rs:
                spiller1Poeng += 1
                print("\nSpiller 1: Korrekt")
            else:
                print("\nSpiller 1: Feil")
                
            if spiller2Svar == rs:
                spiller2Poeng += 1
                print("Spiller 2: Korrekt\n")
            else:
                print("Spiller 2: Feil\n")
    print(f"\nSpiller 1 poeng: {spiller1Poeng}")
    print(f"Spiller 2 poeng: {spiller2Poeng}")
