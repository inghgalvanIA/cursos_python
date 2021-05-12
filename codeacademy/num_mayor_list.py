list3 = []
#Write your function here
def larger_sum(lst1,lst2):

    for index in range (0,3):
        if lst1[index] > lst2[index]:
            list3.append(lst1[index])
        elif lst2[index] > lst1[index]:
            list3.append(lst2[index])
        else:
            list3.append(lst1[index])
    return list3

#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))