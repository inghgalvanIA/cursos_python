

cadenas = "Esto es una cadena"

def get_length(cadena):
  count = 0

  for cadena in cadenas:
      count = count + 1
     
  return count

print(get_length(cadenas))