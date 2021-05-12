# Your code below:
single_digits =[0,1,2,3,4,5,6,7,8,9]
print(single_digits)
squares=[]
cubes=[]

for digit in single_digits:
  print(digit)
  square = [digit ** 2]
  print(square)
  squares += square
  cube = [digit ** 3]
  print(cube)
  cubes += cube
print(squares)
print(cubes)
