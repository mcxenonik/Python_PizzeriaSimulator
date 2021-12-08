from ProductInterface import ProductInterface


class Product(ProductInterface):
    def __init__(self, new_id, new_name, new_price):
        super().__init__()

        self._ID = new_id
        self._name = new_name
        self._price = new_price


    def getID(self):
        return self._ID


    def getName(self):
        return self._name


    def getPrice(self):
        return self._price