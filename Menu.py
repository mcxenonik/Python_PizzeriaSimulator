from Pizza import Pizza
from Drink import Drink

class Menu:
    def __init__(self, textMenu=None):
        self._productList  = []

        if (textMenu is not None):
            self.creatMenu(textMenu)


    def getProductList(self):
        return self._productList


    def getProductByID(self, productID):
        return self._productList[productID]


    def creatMenu(self, textMenu):
        for product in textMenu:
            if (product.type == "pizza"):
                new_product = Pizza(len(self._productList), product.name, product.price, product.preapeTime, product.eatingTime)
            elif (product.type == "drink"):
                new_product = Drink(len(self._productList), product.name, product.price, product.drinkingTime)

            self._productList.append(new_product)