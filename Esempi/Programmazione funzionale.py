#PASSO FUNZIONE COME PARAMETRO DI UNA FUNZIONE

def apply_twice(func, arg):         #Passo una funzione da eseguire e il parametro da passargli
   return func(func(arg))           #Chiamo func due volte, sommo per due volte 5

def add_five(x):
   return x + 5

print(apply_twice(add_five, 10))

##PURE FUNCTION -> OUTPUT DIPENDE SOLO DAI PARAMTERI CHE PASSO COME ARGOMENTI DELLA FUNZIONE

##MAP  ##
# TAKE FUNCTION AND ITERABLE -> RESTITUISCE ITERABLE CON FUNZIONE APPLICATA OGNI ELEMENTO
def add_five(x):
  return x + 5

nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums)) #CREO LISTA, ad ogni elemento di nums sommo 5
print(result)

#The function FILTER filters an iterable by removing items that don't match a predicate
nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x: x%2==0, nums))      #se non è divisibile per 2 lo elimino da nums
print(res)