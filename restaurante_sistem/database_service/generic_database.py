class GenericDataBase:
    """
    this is a class that represts the student database and implements some database operations
    """


    def __init__(self,database_name:str)->None:
        self.name=database_name

        self.data = {}
        self.id_counter += 1
    
    def create(self, data: dict)->int:
        """this method add register in database and return the associeted ID

        Args:
            data (dict): data associated to an student 

        Returns:
            int: ID of the student
        """
        self.data[self.id_counter] = data
        self.id_counter += 1

        return self.id_counter -1
    
    def read(self, _id:int)->dict:
        return self.data[_id]

    def update(self, _id, data)->None:
        self.data[_id] = data


    def delete(self, _id: int)->None:
        del self.data[_id]

    def get_all_data(self)->dict:
        return self.data

    def count(self)->int:
        return len(self.data)
                      