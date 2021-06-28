"""
kgargs es igual que trabajar con args con la diferencia que en vez de trabajar con
tuplas estaremos trabajando con diccionarios

**kargs

"""

def usuarios(**kwargs):
    print(kwargs)
    print(type(kwargs))

usuarios(eduardo=[10,10,8],fernando=[10,9,9])


