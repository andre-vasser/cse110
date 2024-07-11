scripture = ("All covenants, contracts, bonds, obligations, oaths, vows, performances, connections, associations, or expectations, that are not made and entered into and sealed by the Holy Spirit of promise, of him who is anointed, both as well for time and for all eternity, and that too most holy, by revelation and commandment through the medium of mine anointed, whom I have appointed on the earth to hold this power (and I have appointed unto my servant Joseph to hold this power in the last days, and there is never but one on the earth at a time on whom this power and the keys of this priesthood are conferred), are of no efficacy, virtue, or force in and after the resurrection from the dead; for all contracts that are not made unto this end have an end when men are dead.")
words = 0
vowels = 0
consonants = 0
characters = 0
for i in scripture:
    characters += 1
    if i == " ":
       words += 1 
    elif i.lower() == "a"or i.lower() =="e" or i.lower() == "i"or i.lower() == "o" or i.lower() == "u":
        vowels += 1
    elif i != "," or i != "(" or i != ")" or i != ";" or i != ".":
        consonants += 1
words += 0

sum = words +vowels +consonants
print (f"Total: {characters}")
print(f"Palavras: {words}")
print(f"Vowels:     {vowels}")
print(f"Consonants: {consonants}")
print(sum)



    