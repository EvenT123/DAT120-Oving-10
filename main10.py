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

saListe = []
spillerListe = []
spillerPoeng = []
runOnce = 0
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
            while runOnce == 0:
                antallSpillere = int(input("Skriv inn antall spillere: "))
                teller = 1
                for spillere in range(antallSpillere):
                    spillerListe.append(input(f"Navnet til spiller {teller}: "))
                    spillerPoeng.append(0)
                    teller += 1
                runOnce = 1
            
            print(str(x))
            
            teller = 0
            tilbakemelding = ""
            for spillere in range(antallSpillere):
                svar = int(input(f"Velg et svaralternativ for spiller {spillerListe[teller]}: "))
                if svar == rs:
                    spillerPoeng[teller] += 1
                    tilbakemelding += f"Spiller {spillerListe[teller]}: Korrekt\n"
                else:
                    tilbakemelding += f"Spiller {spillerListe[teller]}: Feil\n"
                teller += 1
                
            print(x.korrekt_svar_tekst() + "\n")
            print(tilbakemelding)
        
    
    høyestPoengsum = max(spillerPoeng)
    vinnerIndex = spillerPoeng.index(høyestPoengsum)
    print(f"{spillerListe[vinnerIndex]} er vinneren med {spillerPoeng[vinnerIndex]} poeng!")