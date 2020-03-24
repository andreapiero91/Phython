## METACARATTERI  -> ESPRESSIONI REGOLARI ##

import re

# PUNTO (.) SIGNIFICA QUALSIASI CARATTERE, eccetto new line
pattern = r"gr.y"

if re.match(pattern, "grey"): #TRUE, cerca gr(qualsiasi carattere)y
   print("Match 1")

if re.match(pattern, "gray"):  #TRUE
   print("Match 2")

if re.match(pattern, "blue"):  #FALSE
   print("Match 3")

#METACARATTERI ^ E $.
#INIZIO E FINE DI UNA STRINGA

pattern = r"^gr.y$" #Inizia con gr. poi un qualsiasi carattere e finisce con y

if re.match(pattern, "grey"):   #true
   print("Match 1")

if re.match(pattern, "gray"): #true
   print("Match 2")

if re.match(pattern, "stingray"): #false, non inizia con gr
   print("Match 3")

######## CHARACTER CLASSES #######

pattern = r"[aeiou]"  #Match uno solo di questi caratteri?

if re.search(pattern, "grey"): #true
   print("Match 1")

if re.search(pattern, "qwertyuiop"): #true
   print("Match 2")

if re.search(pattern, "rhythm myths"): #false, non si trova nessuna di quelle lettere
   print("Match 3")

## ES 2 CHARACTER CLASSES ##

pattern = r"[A-Z][A-Z][0-9]" #Ogni lettera maiuscola, seguita da ogni lettera maiuscola, seguita da una cifra

if re.search(pattern, "LS8"): #True, maiuscola maiuscola numero
   print("Match 1")

if re.search(pattern, "E3"): #False, ho solo una maiuscola
   print("Match 2")

if re.search(pattern, "1ab"): #False, inizia con un numero
   print("Match 3")

## METACARATTERI NUMERO RIPETIZIONI  *, +, ?, { and }.

#The metacharacter * means "zero or more repetitions of the previous thing".
#It tries to match as many repetitions as possible.
# The "previous thing" can be a single character, a class, or a group of characters in parentheses.

#The metacharacter +, means "one or more repetitions

#The metacharacter ? means "zero or one repetitions".

#{Curly braces} can be used to represent the number of repetitions between two numbers.
#The regex {x,y} means "between x and y repetitions of something".
#"9{1,3}$" matches string that have 1 to 3 nines.

#Another important metacharacter is |.
#This means "or", so (red|blue) matches oppure "red" or "blue".

#ES 1
pattern = r"egg(spam)*" #egg seguito da zero o più spam

if re.match(pattern, "egg"):
   print("Trovato1")

if re.match(pattern, "eggspamspamegg"):
   print("Trovato2")

if re.match(pattern, "spam"):  #non inizia con spam
   print("Trovato3")

#################
#More useful special sequences are \d, \s, and \w.
#These match digits, whitespace, and word characters respectively.
#In ASCII mode they are equivalent to [0-9], [ \t\n\r\f\v], and [a-zA-Z0-9_].
#In Unicode mode they match certain other characters, as well. For instance, \w matches letters with accents.
#Versions of these special sequences with upper case letters - \D, \S, and \W - mean the opposite to the lower-case versions.
# For instance, \D matches anything that isn't a digit.
pattern = r"(\D+\d)" #uno o più ripetizioni di qualcosa non è un numero, seguito da un numero

match = re.match(pattern, "Hi 999!") #true

if match:
   print("Match_es 1")

match = re.match(pattern, "1, 23, 456!") #false, inizia con numero
if match:
   print("Match_es 2")

match = re.match(pattern, " ! $?")      #false, non ho numero dopo
if match:
    print("Match_es 3")

## VERIFICO SE E' UN EMAIL

pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
str = "Please contact info@sololearn.com for assistance"

match = re.search(pattern, str)
if match:
   print(match.group()) #STAMPA L'EMAIL