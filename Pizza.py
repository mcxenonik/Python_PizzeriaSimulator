from Product import Product


class Pizza(Product):
    def __init__(self, new_id, new_name, new_price, new_prepareTime, new_eatingTime):
        super().__init__(new_id, new_name, new_price, new_prepareTime)

        self._eatingTime = new_eatingTime


    def getEatingTime(self):
        return self._eatingTime
