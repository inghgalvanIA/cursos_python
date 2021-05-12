mensaje = "Este es un texto un poco grande en cuanto a longitud de caracteres se refiere"

resultado = mensaje.count("e")#se va a contar el numero de veces que se repite el caracter
resultado_uno = "texto" in mensaje #entrega un valor bolleano si o no aparece en la cadena
resultado_dos = "texto" not in mensaje#negar la funcion in
resultado_tres = mensaje.find("texto")#encontrar el inicio indice de la cadena selecionada
resultado_cuatro = mensaje.startswith("Este")#pregunta si el inicio del mensaje inicia asi
resultado_cinco = mensaje.endswith ("refiere")#pregunta si el final del mensaje aparece asi

print (resultado)
print (resultado_uno)
print (resultado_dos)
print (resultado_tres)
print (resultado_cuatro)
print (resultado_cinco)
