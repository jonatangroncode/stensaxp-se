# Sten Sax Påse - Ett Konsolbaserat Spel

Detta är ett konsolbaserat sten, sax, påse-spel där du spelar mot datorn. Datorn väljer slumpmässigt mellan sten, sax eller påse, och du ska göra samma sak för att se vem som vinner.

## Hur man kör spelet

Följ stegen nedan för att spela:

1. **Installera Python:**  
   Se till att du har Python installerat på din dator. Du kan ladda ner Python från [Python.org](https://www.python.org/).
   Om du använder VScode behöver du även lägga till python extensions i VScode.

2. **Klona eller ladda ner projektet:**
   Du kan klona projektet från GitHub eller ladda ner filerna.

3. **Navigera till projektmappen i din terminal/kommandoprompt:**
   Använd kommandot `cd` för att gå till den mapp där spelet finns.

4. **Kör spelet:**
   Kör följande kommando i terminalen/kommandoprompten för att starta spelet:
   ```bash
   python rockpaperscissor.py
   ```
   Alternativt kan du skriva:
   ```bash 
   python3 rockpaperscissor.py


   ## Hur man spelar

   1. När spelet startar kommer du att bli tillfrågad att välja mellan "sten", "sax" eller "påse".
      - Skriv ditt val och tryck på Enter. Valet är inte skiftlägeskänsligt, så du kan skriva "sten", "Sten" eller "STEN", och alla tolkas som samma sak.
      
   2. Datorn gör samtidigt ett slumpmässigt val mellan "sten", "sax" eller "påse".
   
   3. Spelet avgör vinnaren baserat på följande regler:
      - **Sten slår sax** (sten vinner).
      - **Sax slår påse** (sax vinner).
      - **Påse slår sten** (påse vinner).
      - Om spelaren och datorn väljer samma sak blir det oavgjort.
   
   4. Spelet visar ett meddelande om resultatet – om du vann, om datorn vann eller om det blev oavgjort.
   
   5. Efter varje omgång får du frågan om du vill spela igen:
      - Om du skriver "ja", startar en ny omgång.
      - Om du skriver "nej" (eller något annat), avslutas spelet med ett tackmeddelande.
   
    
      ## Krav

      - **Python 3.x eller senare**: Programmet är skrivet i Python, så du behöver ha Python installerat på din dator. Du kan ladda ner den senaste versionen från [Python.org](https://www.python.org/).
      - **random-modulen**: Detta är en standardmodul i Python som används för att göra slumpmässiga val. Den installeras automatiskt tillsammans med Python, så du behöver inte installera något extra.
   