from argparse import ArgumentParser, Namespace
from ast import Str

from restaurante_sistem import(
    ClientesDataBase,
    EmpleadosDataBase,
    get_clientes_metrics,
    get_empleados_metrics
)

def execute(args: Namespace)->None:
    if args.database_name == "clientes":
        clientes_database= ClientesDataBase()
    if args.database_name == "empleados":
        database = EmpleadosDataBase()
       
    while True:
        #clientes: primer nombre, edad , valor_factura
        #emleados: primer nombre, edad, salario
        #la letra e identifica estudiantes y la letra p a profesores
        user_input = input("ingrese los datos del individuo:")

        identifier, first_name, age, valor_factura_or_salario = user_input.split(" ")
        if identifier =="c":
            person_id = database.create({
                "first_name": first_name,
                "age": int(age),
                "valor_factura":int(valor_factura_or_salario)
            })
            get_clientes_metrics(database)

        if identifier =="e": 
            person_id = database.create({
                "first_name": first_name,
                "age": int(age),
                "salario":float(semester_or_salario)
            })   

            get_emoleados_metric(database)
        #print(students_database.read(student_id))
        print(clientes_database.get_all_data())
        print(clientes_database.count())
        

        #print(first_name)
        #print(age)
        #print(semester)




def main()->None:
    parser = ArgumentParser()

    parser.add_argument(
        "-dn", "--database-name", type=str,
        choices=["clientes", "empleados", "athers"]
    )

    args = parser.parse_args()
    print(args)



if __name__ == "__main__":
    main()
