# Filstruktur og oppskrift 
Hei og velkommen til vår theater-database. Dette er en oppskrift på hvordan programmet vårt skal kjøres, 
samt en oversikt over filene vi bruker. 

### Oversikt over filer: 
- Theater.db: Dette er den tomme databasefilen som få matet inn data når man kjører programmet. 
- Theater.sql: Dette er sql filen som oppretter alle tabellene i databasen vår. 
- Insertion.sql: Dette er sql filen som setter inn data gitt i oppgaven. 
- Main.py: Python fil som kjører programmet i terminalen. 
- InitializeTheater.py: Python fil som leser inn "Insertion.sql" og mater dataen inn i "Theater.db". Dette er da filen som løser brukstilfelle 1. 
- InputSeats.py: Python fil som leser inn hjelpefilene gitt i oppgaven, "gamle-scene.txt" og "hovedscenen.txt". Ved hjelp av disse setter filen stolene inn i databasen. I tillegg er det denne filen som legger inn opptatte seter på gitt dato i hjelpefilene (brukstilfelle 2). Standardbrukeren som står for kjøpet av de opptatte setene opprettes også i denne filen. 
- FindSeats.py: Løser brukstilfelle 3. Den finner 9 ledige stoler på samme rad til og returnerer summen av hva disse billettene koster. 
- FindPlayOnDate.py: Løser brukstilfelle 4 der det tas inn en dato og returneres hvilke forestillinger som spilles og antall billetter solgt denne datoen. 
- FindActor.py: Løser brukstilfelle 5. Dette skulle egentlig bare være en sql fil, men siden vi har valgt å løse programmet slik at alt kjøres i terminalen, så har vi laget et python script for denne også. 
- FindBestPerformance.py: Løser brukstilfelle 6. Funksjonen finner hvilke forestillinger som har solgt flest billetter, der antall solgte billetter er sortert i synkende rekkefølge. Dette også skal bare være en SQL-fil, men vi har valgt å løse denne på samme måte som forrige oppgave pga at det skal kjøres i terminalen. 
- FindCoActors.py: Løser brukstilfelle 7. Tar inn et skuespillernavn og returnerer navnet på skuespilleren, hvilken akt og hvilket skuespill dette skjedde. 

### Oppskrift på hvordan man bruker programmet
- Åpne "Main.py"
- Kjør programmet og følg instruksene gitt i terminalen:)

