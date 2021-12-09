from Waiter import Waiter
from Customer import Customer
from Table import Table
from Order import Order
from Menu import Menu

from random import randint


class Pizzeria:
    def __init__(self):
        self._waitersList = []
        self._customersList = []
        self._tablesList = []
        self._orderList = []
        self._menu = None

        self._creatMenu()


    def getWaitersList(self):
        return self._waitersList


    def getCustomersList(self):
        return self._customersList


    def getTableList(self):
        return self._tablesList


    def getOrderList(self):
        return self._orderList


    def getMenu(self):
        return self._menu


    def getWaiterByID(self, waiterID):
        return self._waitersList[waiterID]


    def getCustomerByID(self, customerID):
        return self._customersList[customerID]


    def getTableByID(self, tableID):
        return self._tablesList[tableID]


    def getOrderByID(self, orderID):
        return self._orderList[orderID]


    def getProductByID(self, productID):
        return self._menu[productID]

    def _creatMenu(self):
        self._menu = Menu()


    def addWaiter(self):
        new_waiter = Waiter(len(self._waitersList))

        self._waitersList.append(new_waiter)

    
    def addCustomer(self):
        new_customer = Customer(len(self._customersList), randint(0, 4))

        self._customersList.append(new_customer)


    def addTable(self):
        new_table = Table(len(self._tablesList), randint(1, 5))

        self._tablesList.append(new_table)


    def addOrder(self, new_order):
        self._orderList.append(new_order)
