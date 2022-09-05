def get_age_mean(database)->float:
    data = database.get_all_data()

    mean=0
    for clientes_data in data:
        mean += clientes_data["age"]
    return mean/database.count()



def get_semester_mean(database)->float:
    data = database.get_all_data()

    mean=0
    for clientes_data in data:
        mean += clientes_data["semester"]
    return mean / database.count()

def get_differents_letters_mean(database)->float:
    data = database.get_all_data()

    mean=0
    for clientes_data in data:
        lower_name = clientes_data["first_name"].lower()
        differents_letters = set(clientes_data["lower_name"])
        mean +=len(differents_letters)

    return mean / database.count()
    


def get_clientes_metrics(database):
    print(f"age_mean: {get_age_mean(database)}")
    print(f"semester_mean:{get_semester_mean(database)}")
    print(f"Different_letters_mean:{get_differents_letters_mean(database)}")
    print(f"clientes_count: {database.count()}")