## SET : Sets are data structures, similar to lists or dictionaries.

#NON SONO ORDINATE, QUINDI NON USO INDICE
#NON HANNO ELEMENTI DUPLICATI

num_set = {1, 2, 3, 4, 5}
second = {4, 5, 6, 7, 8, 9}

word_set = set(["spam", "eggs", "sausage"])

#IN e NOT IN?
print(3 in num_set)             #3 è presente in num_set?
print("spam" not in word_set)

#STAMPO SET
print(num_set)

#AGGIUNGO -7 AL SET
num_set.add(-7)

#RIMUOVO 3 DAL SET
num_set.remove(3)

print(num_set)

print("######################")
## METODI PER COMBINARE ELEMENTI ##
print(num_set)
print(second)
print("####")

print(num_set | second) #unisco i due set
print(num_set & second) #Solo elementi che sono in entrambi i set
print(num_set - second) #Elementi che sono nel primo set ma non nel secondo
print(second - num_set)
print(num_set ^ second) #Elementi che sono in un set ma noon in entrambi

#When to use a dictionary:
# 1- When you need a logical association between a key:value pair.
# 2- When you need fast lookup for your data, based on a custom key.
# 3- When your data is being constantly modified. Remember, dictionaries are mutable.

#When to use the other types:
# 1- Use LISTS if you have a collection of data that does not need random access. Try to choose lists when you need a simple, iterable collection that is modified frequently.
# 2- Use a SET if you need uniqueness for the elements.
# 3- Use TUPLES when your data cannot change.