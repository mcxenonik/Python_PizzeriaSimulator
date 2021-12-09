from random import randint

from Person import Person
from CustomerStates import CustomerStates
from TaskTypes import TaskTypes


class Waiter(Person):
    def __init__(self, new_id):
        super().__init__(new_id)

        self._taskQueue = []


    def addTask(self, new_task):
        self._taskQueue.append(new_task)


    def getNumberOfTasks(self):
        return len(self._taskQueue)


    def doTask(self, sim_pizzeria):
        if (len(self._taskQueue) == 0):
            # print("KELNER:", self._ID, "OCZEKUJE NA ZADANIE")
            self.printLog(None)
            return

        task = self._taskQueue.pop(0)
        taskType = task.getTaskType()
        customerId = task.getCustomerID()

        if (taskType == TaskTypes.GM):
            sim_pizzeria.getCustomerByID(customerId).setState(CustomerStates.SO)
            # print("KELNER:", self._ID, "PODAJE KARTE DAN KLIENTOWI:", customerId)
            self.printLog(taskType, customerId)

        elif (taskType == TaskTypes.CO):
            sim_pizzeria.getCustomerByID(customerId).setState(CustomerStates.WFPO)
            waitTime = randint(1, 5)
            sim_pizzeria.getCustomerByID(customerId).setWaitTime(waitTime)
            # print("KELNER:", self._ID, "ODBIERA ZAMOWIENIE OD KLIENTA:", customerId)
            # print("CZAS OCZEKIWANIA:", waitTime)
            self.printLog(taskType, customerId, waitTime)

        elif (taskType == ""):
            pass

        else:
            pass


    def printLog(self, taskType, customerId=None, waitTime=None):
        if (taskType == None):
            print("KELNER:", self._ID, "OCZEKUJE NA ZADANIE")

        elif (taskType == TaskTypes.GM):
            print("KELNER:", self._ID, "PODAJE KARTE DAN KLIENTOWI:", customerId)

        elif (taskType == TaskTypes.CO):
            print("KELNER:", self._ID, "ODBIERA ZAMOWIENIE OD KLIENTA:", customerId)
            print("CZAS OCZEKIWANIA:", waitTime)

        elif (taskType == ""):
            pass

        else:
            pass