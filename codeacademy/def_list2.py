#Write your function here
def add_greetings(names):
  
  hello = []
  
  for name in names:
    hello.append("Hello, "+ name)
  return hello
  
#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))