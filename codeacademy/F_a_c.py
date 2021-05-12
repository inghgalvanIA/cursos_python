f_temp = input("¿que temperatura quieres convertir?")


def f_to_c(f_temp):
    c_temp = None
    c_temp = (int(f_temp) - 32) * 5/9
    return c_temp

resultado_final = f_to_c(f_temp)
print(str(resultado_final))