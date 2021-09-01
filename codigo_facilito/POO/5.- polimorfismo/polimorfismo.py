def retornaElMayor(a,b):
    #metodos de cualquier tipo dependiendo del valor retornara
    #si son numeros retornara el mayor numero
    #si son lista retornara la lista con mayor elementos
    #si son cadenas  aacomodara por alfabeticamente

    if isinstance(a,int) and isinstance(b,int):
        if a > b:
            return a
        return b

    if isinstance(a,str) and isinstance(b,str):
      palabras = [a,b]
      palabras.sort()
      return palabras[0]

    if isinstance(a,list) and isinstance(b,list):
       if len(a) > len(b):
           return a
        return b

    print(retornaElMayor(10,20))