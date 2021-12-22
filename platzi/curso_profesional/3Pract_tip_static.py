#pip install mypy

#archivo palindromo

#haberiguar si una cadena de caracteres es un palindromo
# 
# 


def is_palindrome(string:str) -> bool:
    string = string.replace(" ","").lower()
    return  string == string [::-1]

def run():
    print(is_palindrome("AnA"))   

if __name__ == "__main__":
    run()