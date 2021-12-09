from random import randint

from TaskTypes import TaskTypes


class Task:
    def __init__(self, new_customerID, new_taskType):
        self._ID = randint(0, 100000)
        self._customerID = new_customerID
        self._taskType = new_taskType


    def getID(self):
        return self._ID


    def getCustomerID(self):
        return self._customerID


    def getTaskType(self):
        return self._taskType