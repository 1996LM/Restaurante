from argparse import ArgumentParser, Namespace
from ast import Str

from restaurant_sistem import(
    studentsDatabase,
    TeachersDataBase,
    get_students_metrics,
    get_teachers_metrics
)

def execute(args: Namespace)->None:
    if args.database_name == "students":
        students_database= StudentsDataBase()
    if args.database_name == "teachers":
        database = TeachersDataBase()
       
    while True:
        #Estudiantes: primer nombre, edad , semestre
        #Profesores: primer nombre, edad, salario
        #la letra e identifica estudiantes y la letra p a profesores
        user_input = input("ingrese los datos del individuo:")

        identifier, first_name, age, semester_or_salary = user_input.split(" ")
        if identifier =="e":
            person_id = database.create({
                "first_name": first_name,
                "age": int(age),
                "semester":int(semester_or_salary)
            })
            get_students_metrics(database)

        if identifier =="p": 
            person_id = database.create({
                "first_name": first_name,
                "age": int(age),
                "salary":float(semester_or_salary)
            })   

            get_teachers_metric(database)
        #print(students_database.read(student_id))
        print(students_database.get_all_data())
        print(students_database.count())
        

        #print(first_name)
        #print(age)
        #print(semester)




def main()->None:
    parser = ArgumentParser()

    parser.add_argument(
        "-dn", "--database-name", type=str,
        choices=["students", "teacher", "athers"]
    )

    args = parser.parse_args()
    print(args)



if __name__ == "__main__":
    main()
