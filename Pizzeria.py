from Waiter import Waiter
from Customer import Customer
from Table import Table
from Order import Order

from random import randint


class Pizzeria:
    def __init__(self):
        self._waitersList = []
        self._customersList = []
        self._tablesList = []
        self._orderList = []


    def getWaitersList(self):
        return self._waitersList


    def getCustomersList(self):
        return self._customersList


    def getTableList(self):
        return self._tablesList


    def getOrderList(self):
        return self._orderList


    def addWaiter(self):
        new_waiter = Waiter(len(self._waitersList))

        self._waitersList.append(new_waiter)

    
    def addCustomer(self):
        new_customer = Customer(len(self._customersList), "NEW", randint(0, 3))

        self._customersList.append(new_customer)


    def addTable(self):
        new_table = Table(len(self._tablesList), randint(1, 5))

        self._tablesList.append(new_table)


    def addOrder(self, new_order):
        self._orderList.append(new_order)
