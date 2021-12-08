from Product import Product


class Pizza(Product):
    def __init__(self, new_id, new_name, new_price, new_prepareTime, new_eatingTime):
        super().__init__(new_id, new_name, new_price)

        self._prepareTime = new_prepareTime
        self._eatingTime = new_eatingTime


    def getPrepareTime(self):
        return self._prepareTime


    def getEatingTime(self):
        return self._eatingTime
