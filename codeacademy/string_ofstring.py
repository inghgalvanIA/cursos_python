# Write your check_for_name function here:

def check_for_name(sentence,name):
    
    resultado = False 

    tranf_minusculas = sentence.title()

    lista_res = tranf_minusculas.split()

    for index in lista_res:
        if index == name:
            resultado = True
        else:
            continue
    
    return resultado

# Uncomment these function calls to test your  function:
#print(check_for_name("My name is Jamie", "Jamie"))
# should print True
#print(check_for_name("My name is jamie", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))
# should print False