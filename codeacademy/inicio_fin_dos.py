# Write your substring_between_letters function here:

def substring_between_letters(word,letter__start,letter__end):
    start = None
    end = None
    contador = 0
    inicio = word.count(letter__start)
    final = word.count(letter__end)
    print(inicio)
    print(final)

    index_inicio = word.index("")
    


# Uncomment these function calls to test your function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
#print(substring_between_letters("apple", "p", "c"))
# should print "apple"