from argparse import ArgumentParser
#ayuda a definir argumentos que le puedo pasar a un programa
def main():
    parser = ArgumentParser()
    
    parser.add_argument(
        "-dn", "--database-name", type=str, 
        choices = ["students", "teachers", "others"]

    )
    args = parser.parse_args()
    print(args)

if __name__ =="__main__":
    main()