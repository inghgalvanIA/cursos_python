"""
 ¿y si queremos crear un archivo propio? Con Python podemos hacer precisamente eso. Resulta que nuestra función open () que estamos usando para abrir un archivo para leer necesita otro argumento para abrir un archivo para escribir.
 
"""

with open('bad_bands.txt', 'w') as bad_bands_doc:

  bad_bands_doc.write('The Beatles')
  # Weren't expecting THAT were you??