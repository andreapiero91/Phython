########    ESPRESSIONI REGOLARI    #########
import re

pattern = r"spam"  #con r indico che è un espressione regolare

## MATCH: True se stringa2 inizia con pattern
if re.match(pattern, "spamspamspam"): # (pattern,stringa2)
   print("Match")                     #Stampa questo poichè spamspam inizia con spam(pattern)
else:
   print("No match")

## SEARCH: True se trova pattern in qualsiasi posizione della stringa
match = re.search(pattern, "eggspamsausagespam") #cerca spam(pattern) in tutta la stringa
if match:
    print("Match")
    print(match.group()) #Quale è la Stringa trovata?
    print(match.start()) #Posizione iniziale della prima occorenza trovata
    print(match.end())   #Posizione finale della prima occorrenza trovata
    print(match.span())  #(start, end)
else:
    print("No match")

## FINDALL ## #mette in una lista tutte le occorrenze di pattern trova
print(re.findall(pattern, "eggspamsausagespam"))

## SOSTITUZIONE IN STRINGA ##

str = "My name is David. Hi David."
pattern = r"David"
newstr = re.sub(pattern, "Amy", str) #Sostituisco David con Amy in ogni posizione
print(newstr)