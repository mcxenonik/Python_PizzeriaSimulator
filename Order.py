
class Order:
    def __init__(self, new_id, new_personID, new_productList):
        self._ID = new_id
        self._personID = new_personID
        self._isReady = False
        self._isPaid = False
        self._waitTime = 0
        self._productList  = new_productList

        self._setWaitTime()


    def getID(self):
        return self._ID


    def getPersonID(self):
        return self._personID


    def isReady(self):
        return self._isReady


    def isPaid(self):
        return self._isPaid


    def getProductList(self):
        return self._productList


    def _setWaitTime(self):
        for product in self._productList:   
            self._waitTime += product.getPrepareTime()


    def decreaseWaitTime(self):
        self._waitTime -= 1

        if (self._waitTime == 0):
            self._isReady = True
