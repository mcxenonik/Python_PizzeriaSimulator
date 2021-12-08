from Product import Product


class Drink(Product):
    def __init__(self, new_id, new_name, new_price, new_drinkingTime):
        super().__init__(new_id, new_name, new_price)

        self._drinkingTime = new_drinkingTime


    def getPrepareTime(self):
        return self._drinkingTime