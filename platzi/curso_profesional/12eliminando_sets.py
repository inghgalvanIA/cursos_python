# eliminar los elementos repetidos de una lista
#[1,1,2,2,4] -> [1,2,4]

my_list = [1,1,2,2,4]

def remove_duplicate(my_list):
    the_set = set(my_list)
    list_result = list(the_set)
    return list_result


print(remove_duplicate(my_list))