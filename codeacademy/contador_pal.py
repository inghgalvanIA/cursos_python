# Write your count_multi_char_x function here:
def count_multi_char_x(wordl,words):
    resultado = wordl.count(words)
    return resultado

# Uncomment these function calls to test your function:
print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1