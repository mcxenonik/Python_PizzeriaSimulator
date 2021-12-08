from random import randint


class Task:
    def __init__(self, new_personID, new_taskType):
        self._ID = randint(0, 1000)
        self._personID = new_personID
        self._taskType = new_taskType


    def getID(self):
        return self._ID


    def getPersonID(self):
        return self._personID


    def getTaskType(self):
        return self._taskType