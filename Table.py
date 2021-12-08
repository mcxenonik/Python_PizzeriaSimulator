class Table:
    def __init__(self, new_id, new_size):
        self._ID = new_id
        self._size = new_size
        self._isFull = False
        self._groupID = None
        self._customersIDList = []


    def getID(self):
        return self._ID


    def getSize(self):
        return self._size


    def isFull(self):
        return self._isFull


    def getGroupID(self):
        return self._groupID


    def getCustomersIDList(self):
        return self._customersIDList


    def addCustomerToTable(self, new_customer):
        self._customersIDList.append(new_customer.getID())

        if (self._groupID is None):
            self._groupID = new_customer.getGroupID()

        if (len(self._customersIDList) == self._size):
            self._isFull = True


    def deleteCustomerFromTable(self, customer):
        # print("CUSID:", customer.getID())
        # print(self._customersIDList)
        self._customersIDList.remove(customer.getID())
        self._groupID = None
        self._isFull = False
