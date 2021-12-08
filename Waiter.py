from random import randint

from Person import Person


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
            return

        task = self._taskQueue.pop(0)
        taskId = task.getTaskType()
        customerId = task.getPersonID()

        # print("TASK TYPE:", taskId)
        # print("CUS ID:", customerId)

        if (taskId == "Karta dan"):
            sim_pizzeria.getCustomersList()[customerId].setState("Zloz zamowienie")
            print("KELNER:", self._ID, "PODAJE KARTE DAN KLIENTOWI:", customerId)

        elif (taskId == "Zlozono zamowienie"):
            sim_pizzeria.getCustomersList()[customerId].setState("Oczekuj na przygotowanie zamówienia")
            waitTime = randint(1, 5)
            sim_pizzeria.getCustomersList()[customerId].setWaitTime(waitTime)
            print("KELNER:", self._ID, "ODBIERA ZAMOWIENIE OD KLIENTA:", customerId)
            print("CZAS OCZEKIWANIA:", waitTime)

        elif (taskId == ""):
            pass

        else:
            pass