ordliste = dict() #Oppretter et dictionary
linjenummer = 0 #Teller for linjenummer
with open("oving_1_rein_tekst.txt") as fil1: #Åpner filen som fil1
    for linje in fil1: #For hver linje i tekstfilen
        linjenummer += 1 #Definerer hvilken linje som blir lest
        ordene = linje.split() #Deler opp linjene til enkeltord
        for ordet in ordene: #For hvert ord i listen med ord
            ordet = ordet.lower() #Endrer ordene slik at de består av bare små bokstaver
            if ordet not in ordliste: #Hvis ordet ikke allerede er i ordlisten
                ordliste[ordet] = linjenummer #Legger ordet til i ordlisten med value linjenummer     
    
    for ordet in ordliste: #For hvert ord i dictionaryet
        print(f"Ordet {ordet} forekommer først i linje {ordliste[ordet]}.") #Skriver ut ordene og linjenumrene