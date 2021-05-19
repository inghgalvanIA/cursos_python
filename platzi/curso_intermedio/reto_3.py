DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run():
    #busqueda de todos los que dominan python
    #all_python_devs = [worker["name"]for worker in DATA if worker["language"]=="python"]
    all_python_devs = list(filter(lambda worker:worker["language"] == "python",DATA))
    all_python_devs = list(map(lambda worker:worker["name"],all_python_devs))
    #busqueda de todos los que pertenecen a Platzi
    # all_worker = [worker_two["name"] for worker_two in DATA if worker_two["organization"] == "Platzi"]
    all_worker = list(filter(lambda worker_two:worker_two["organization"] == "Platzi", DATA))
    all_worker = list(map(lambda worker_two:worker_two["name"],all_worker))

    # #busqueda de todos los adults
    # all_adults = [worker_three["name"]for worker_three in DATA if worker_three["age"] >= 18]
    all_adults = [worker_three["name"] for worker_three in DATA if worker_three["age"] >= 18]
    # #mayores de 30 con firter
    # adults = list(filter(lambda person:person["age"]>= 30, DATA))
    # #reescribir la list adults para solo rtener la variable nombre
    # adults = list(map(lambda person:person["name"],adults))
    adults = [person["name"] for person in  DATA if person["age"] >= 30]


    print("lista de personas que dominan Python")
    for worker in all_python_devs:
        print(worker)
    print("Lista de personas que pertenecen a platzi")
    for worker_two in all_worker:
        print(worker_two)
    print("lista de personas adultas")
    for worker_three in all_adults:
        print(worker_three)
    print("lista de personas mayores de 30")
    for person in adults:
        print(person)

if __name__ == "__main__":
    run()