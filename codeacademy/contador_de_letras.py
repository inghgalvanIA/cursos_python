word = input("ingresa la palabra o texto")
letter = input("ingresa que letra quieres buscar") 

def letter_check(word,letter):
    
    count = 0
    
    for num in word:
        if num == letter:
            count += 1
        else:
            continue
    return count


print(letter_check(word,letter))