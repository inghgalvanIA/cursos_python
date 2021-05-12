#letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:
def unique_english_letters(word):
    contador = 0
    for index in word:
        contador +=1

    print(contador)    

unique_english_letters("holalulu")

# Uncomment these function calls to test your function:
#print(unique_english_letters("mississippi"))
# should print 4
#print(unique_english_letters("Apple"))
# should print 4