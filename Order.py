class Order:
    def __init__(self, new_id, new_personID, new_productList):
        self._ID = new_id
        self._personID = new_personID
        self._isReady = False
        self._productList  = new_productList


    def getID(self):
        return self._ID


    def getPersonID(self):
        return self._personID


    def isReady(self):
        return self._isReady


    def getProductList(self):
        return self._productList
