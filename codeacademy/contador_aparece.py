# Write your count_char_x function here:
def count_char_x(word,letter):
    count = 0

    for index in word:
        if index == letter:
            count += 1
        else:
            continue
    return count

# Uncomment these function calls to test your tip function:
#print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1