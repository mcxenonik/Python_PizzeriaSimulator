from random import randint
from Person import Person
from Task import Task
from CustomerStates import CustomerStates


class Customer(Person):
    def __init__(self, new_id, new_groupID):
        super().__init__(new_id)

        self._groupID = new_groupID
        self._state = CustomerStates.NEW
        self._tableID = None
        self._orderID = None
        self._eatTime = 0
        self._waitTime = 0


    def getGroupID(self):
        return self._groupID


    def getState(self):
        return self._state


    def getTableID(self):
        return self._tableID


    def getOrderID(self):
        return self._orderID


    def getEatTime(self):
        return self._eatTime


    def getWaitTime(self):
        return self._waitTime


    def setTableID(self, new_tableID):
        self._tableID = new_tableID


    def setEatTime(self, new_eatTime):
        self._eatTime = new_eatTime


    def setWaitTime(self, new_waitTime):
        self._waitTime = new_waitTime


    def addEatTime(self, eatTime_to_add):
        self._eatTime += eatTime_to_add


    def decreaseEatTime(self):
        self._eatTime -= 1


    def decreaseWaitTime(self):
        self._waitTime -= 1


    def setState(self, new_state):
        self._state = new_state


    def zajmij_stolik(self, sim_pizzeria):
        for table in sim_pizzeria.getTableList():
            if (table.getGroupID() == self._groupID and not table.isFull()):
                table.addCustomerToTable(self)
                self._tableID = table.getID()
                return "OK"

        for table in sim_pizzeria.getTableList():
            if (table.getGroupID() == None):
                table.addCustomerToTable(self)
                self._tableID = table.getID()
                return "OK"

        return "NOK"


    def zamow_karte_dan(self, sim_pizzeria):
        waitersList = sim_pizzeria.getWaitersList()

        min_tasks = waitersList[0].getNumberOfTasks()
        waiterID = waitersList[0].getID()

        for waiter in waitersList:
            if (waiter.getNumberOfTasks() < min_tasks):
                min_tasks = waiter.getNumberOfTasks()
                waiterID = waiter.getID()

        new_task = Task(self._ID, "Karta dan")
        sim_pizzeria.getWaitersList()[waiterID].addTask(new_task)


    def oczekuj_na_karte_dan(self):
        pass


    def zloz_zamowienie(self, sim_pizzeria):
        waitersList = sim_pizzeria.getWaitersList()

        min_tasks = waitersList[0].getNumberOfTasks()
        waiterID = waitersList[0].getID()

        for waiter in waitersList:
            if (waiter.getNumberOfTasks() < min_tasks):
                min_tasks = waiter.getNumberOfTasks()
                waiterID = waiter.getID()

        new_task = Task(self._ID, "Zlozono zamowienie")
        sim_pizzeria.getWaitersList()[waiterID].addTask(new_task)


    def oczekuj_na_przyjecie_zamowienia(self):
        pass


    def oczekuj_na_przygotowanie_zamowienia(self):
        self.decreaseWaitTime()


    def zjedz(self):
        self.decreaseEatTime()


    def oczekuj_na_rachunek(self):
        pass


    def wez_rachunek(self):
        pass


    def oczekuj_na_pobranie_oplaty(self):
        pass


    def oplac_rachunek(self):
        pass


    def out(self, sim_pizzeria):
        sim_pizzeria.getTableList()[self._tableID].deleteCustomerFromTable(self)
        self._state = CustomerStates.OUT
    

    def doAction(self, sim_pizzeria):
        if (self._state == CustomerStates.NEW):
            result = self.zajmij_stolik(sim_pizzeria)

            if (result == "OK"):
                print("KLIENT:", self._ID, "Z GRUPY:", self._groupID, "ZAJMUJE STOLIK:", self._tableID)
                self._state = CustomerStates.OM
            else:
                print("KLIENT:", self._ID, "Z GRUPY:", self._groupID, "OCZEKUJE NA WOLNY STOLIK")
                self._state = CustomerStates.NEW

        elif (self._state == CustomerStates.OM):
            self.zamow_karte_dan(sim_pizzeria)

            print("KLIENT:", self._ID, "Z GRUPY:", self._groupID, "SIEDZACY PRZY STOLIKU:", self._tableID, "ZAMOWIL KARTE DAN")
            self._state = CustomerStates.WFM

        elif (self._state == CustomerStates.WFM):
            self.oczekuj_na_karte_dan()

            print("KLIENT:", self._ID, "Z GRUPY:", self._groupID, "SIEDZACY PRZY STOLIKU:", self._tableID, "OCZEKUJE NA KARTE DAN")
            self._state = CustomerStates.WFM

        elif (self._state == CustomerStates.SO):
            self.zloz_zamowienie(sim_pizzeria)

            print("KLIENT:", self._ID, "Z GRUPY:", self._groupID, "SIEDZACY PRZY STOLIKU:", self._tableID, "SKŁADA ZAMOWIENIE")
            self._state = CustomerStates.WFAO

        elif (self._state == CustomerStates.WFAO):
            self.oczekuj_na_przyjecie_zamowienia()

            print("KLIENT:", self._ID, "Z GRUPY:", self._groupID, "SIEDZACY PRZY STOLIKU:", self._tableID, "OCZEKUJE NA PRZYJECIE ZAMOWIENIA")
            self._state = CustomerStates.WFAO

        elif (self._state == CustomerStates.WFPO):
            self.oczekuj_na_przygotowanie_zamowienia()

            if (self._waitTime == 0):
                self._state = CustomerStates.E
                self._eatTime = randint(1, 5)
            else:
                print("KLIENT:", self._ID, "Z GRUPY:", self._groupID, "SIEDZACY PRZY STOLIKU:", self._tableID, "OCZEKUJE NA PRZYGOTOWANIE ZAMOWIENIA. POZOSTALO:", self._waitTime)
                self._state = CustomerStates.WFPO

        elif (self._state == CustomerStates.E):
            self.zjedz()

            if (self._eatTime == 0):
                self._state = CustomerStates.WFB
            else:
                print("KLIENT:", self._ID, "Z GRUPY:", self._groupID, "SIEDZACY PRZY STOLIKU:", self._tableID, "SPOZYWA ZAMOWIENIE. POZOSTALO:", self._eatTime)
                self._state = CustomerStates.E

        elif (self._state == CustomerStates.WFB):
            self.oczekuj_na_rachunek()

            print("KLIENT:", self._ID, "Z GRUPY:", self._groupID, "SIEDZACY PRZY STOLIKU:", self._tableID, "OCZEKUJE NA RACHUNEK")
            self._state = CustomerStates.WFB

            self.out(sim_pizzeria)

        elif (self._state == CustomerStates.TB):
            self.wez_rachunek()

            self._state = CustomerStates.WFPB

        elif (self._state == CustomerStates.WFPB):
            self.oczekuj_na_pobranie_oplaty()

            self._state = CustomerStates.WFPB

        elif (self._state == CustomerStates.PB):
            self.oplac_rachunek()

            self._state = CustomerStates.OUT

        elif (self._state == CustomerStates.OUT):
            # self.out(sim_pizzeria)

            print("KLIENT:", self._ID, "Z GRUPY:", self._groupID, "SIEDZACY PRZY STOLIKU:", self._tableID, "ODCHODZI")
            self._state = CustomerStates.OUT
        