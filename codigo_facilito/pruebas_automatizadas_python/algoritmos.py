"""

>>> recursivo = Recursivo()
>>> recursivo.factorial(5)
120

"""

def fibonacci(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number -1) + fibonacci(number - 2)

def palindromo(sentence):

    """Retron verdadero si el parametro es un palindromo
    en caso contrario retrona falso

    sentence -- string o entero

    >>> palindromo("anita lava la tina")
    True
    """
    sentence = str(sentence).lower().replace(" ","")
    return sentence == sentence[::-1]


class Recursivo:
    def factorial(self,number):
        if number == 0:
             return 1
        else:
            return number * self.factorial(number - 1)

