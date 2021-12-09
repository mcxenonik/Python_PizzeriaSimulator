from random import randint

from Person import Person
from CustomerStates import CustomerStates
from TaskTypes import TaskTypes
from Order import Order
from Task import Task


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
            self.printLog(None)
            return

        task = self._taskQueue.pop(0)
        taskType = task.getTaskType()
        customerId = task.getCustomerID()

        if (taskType == TaskTypes.GM):
            sim_pizzeria.getCustomerByID(customerId).setState(CustomerStates.SO)

            self.printLog(taskType, customerId)

        elif (taskType == TaskTypes.CO):
            orderedProductsList = task.getPayload()

            sim_pizzeria.getCustomerByID(customerId).setState(CustomerStates.WFPO)
            orderID = sim_pizzeria.addOrder(customerId, self._ID, orderedProductsList)
            sim_pizzeria.getCustomerByID(customerId).setOrderID(orderID)

            self.printLog(taskType, customerId, orderID)

        elif (taskType == TaskTypes.DO):
            orderID = task.getPayload()
            
            sim_pizzeria.getCustomerByID(customerId).setState(CustomerStates.E)

            self.printLog(taskType, customerId, orderID)
            
        elif (taskType == TaskTypes.GR):
            orderID = task.getPayload()

            sim_pizzeria.getCustomerByID(customerId).setState(CustomerStates.TB)
            sim_pizzeria.getOrderByID(orderID).createReceipt()

            self.printLog(taskType, customerId, orderID)

        elif (taskType == TaskTypes.TR):
            orderID = task.getPayload()

            sim_pizzeria.getCustomerByID(customerId).setState(CustomerStates.PB)

            self.printLog(taskType, customerId, orderID)
        
        else:
            pass


    def printLog(self, taskType, customerId=None, orderID=None):
        if (taskType == None):
            print("KELNER:", self._ID, "OCZEKUJE NA ZADANIE")

        elif (taskType == TaskTypes.GM):
            print("KELNER:", self._ID, "PODAJE KARTE DAN KLIENTOWI:", customerId)

        elif (taskType == TaskTypes.CO):
            print("KELNER:", self._ID, "ODBIERA ZAMOWIENIE:", orderID, "OD KLIENTA:", customerId)

        elif (taskType == TaskTypes.DO):
            print("KELNER:", self._ID, "DOSTARCZA ZAMOWIENIE:", orderID, "DO KLIENTA:", customerId)

        elif (taskType == TaskTypes.GR):
            print("KELNER:", self._ID, "PODAJE RACHUNEK DO ZAMOWIENIA:", orderID, "KLIENTOWI:", customerId)

        elif (taskType == TaskTypes.TR):
            print("KELNER:", self._ID, "POBIERA OPLATE DO ZAMOWIENIA:", orderID, "OD KLIENTA:", customerId)

        else:
            pass