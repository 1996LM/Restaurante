def get_mean_salary(database)->float:
    data = database.get_all_data()

    mean=0
    for empleados_data in data:
        mean += empleados_data["salary"]
    return mean/database.count()

def get_empleados_metrics(database):
    print("="*80)
    print(f"Mean Salary: {get_mean_salary(database)}")
    