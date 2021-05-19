def run():
    my_list = [1,"Hello",True,4.5]
    my_dict ={"name":"Hector","lastname":"Galvan"}

    super_list = [
        {"name":"Hector","lastname":"Galvan"},
        {"name":"Diana","lastname":"Galvan"},
        {"name":"Leonardo","lastname":"Ruiz"},
        {"name":"Luis","lastname":"Dias"}
    ]

    super_dict = {
        "natrual_nums":[1,2,3,4,5,6],
        "integer_nums":[-1,-2,0,1,2],
        "float_nums":[1.1,4.5,6.43]
    }

    for key, value in super_dict.items():
        print(key, "-", value)

    for value_list in super_list:
        print(value_list)

if __name__ == "__main__":
    run()