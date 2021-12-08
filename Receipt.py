class Receipt:
    def __init__(self, new_id, new_order):
        self._ID = new_id
        self._order = new_order
        self._isPaid = False
        self._totalPrice = self._countPrice()


    def getID(self):
        return self._ID


    def getOrderID(self):
        return self._order.getID()


    def isPaid(self):
        return self._isPaid


    def getTotalPrice(self):
        return self._totalPrice


    def _countPrice(self):
        productList = self._order.getProductList()

        for product in productList:
            self._totalPrice += product.getPrice()