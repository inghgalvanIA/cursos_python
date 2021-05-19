
def palindromo(string_user):
    assert len(string_user)>0,"Nose puede ingresar una cadena vacia"
    return string_user == string_user[::-1]
  



def run():
    valor = input("Ingresa un valor para verificar si es palindromo")
    print(palindromo(valor))
    

if __name__ == "__main__":
    run()