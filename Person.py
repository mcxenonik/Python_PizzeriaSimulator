from PersonInterface import PersonInterface


class Person(PersonInterface):
    def __init__(self, new_id):
        super().__init__()

        self._ID = new_id


    def getID(self):
        return self._ID

