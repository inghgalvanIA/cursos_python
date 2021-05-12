def conversion(cantidad):
    mex_col=145.07 #peso colombiano
    return mex_col * cantidad

def run():
    print("$$$CALCULADORA DE DIVISAS$$$$")
    print("convierte pesos mexicanos a pesos colombianos ")

    cantidad = float(input("ingresa la cantidad a convertir en MXN"))

    total = conversion(cantidad)

    print("${} pesos Mexicanos son ${} pesos colombianos ".format(cantidad,total))

run()
