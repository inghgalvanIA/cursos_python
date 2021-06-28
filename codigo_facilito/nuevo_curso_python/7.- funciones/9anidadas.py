"""
funciones anidadas

las funciones pueden ser anidadas
funciones pueden poseer otras funciones

por norma para separa funciones dejamso 2 espacios de linea 
"""

def operacion(cantidad, balance, tipo="deposito"):

    def deposito(cantidad,balance):
        return cantidad + balance

    
    def retiro(cantidad, balance):
        if cantidad <= balance:
            return balance - cantidad
        else:
            return None

    if tipo == "deposito":
        return deposito(cantidad, balance)
    elif tipo == "retiro":
        return retiro(cantidad, balance)
        

resultado = operacion(10,30)
print(resultado)