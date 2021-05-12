list1 = []

#Write your function here
def exponents(bases,powers):
    

    for base in bases:
        for index in powers:
            result = base ** index
            
            list1.append(result)
             
    return list1


#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))