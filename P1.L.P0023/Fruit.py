import re


class Fruit(object):
    def __init__(self):
        self.__fruitId__ = 0
        self.__fruitName__ = ""
        self.__fruitPrice__= 0.0
        self.__fruitQuantity__ = -1
        self.__fruitOrigin__ = ""

    def __inputFruitName__(self):
        while True:
            self.__fruitName__ = input("Please input fruit name: ")
            if not re.fullmatch("^[\\w\\s]{3,100}$", self.__fruitName__):
                print("Valid fruit name length must be higher than 3 and lower than 100. Try again.")
            else:
                break

    def __inputFruitPrice__(self):
        while True:
            try:
                self.__fruitPrice__ = float(input("Please input fruit price: "))
                if self.__fruitPrice__ < 0:
                    print("Fruit price must be a positive value.")
                else:
                    break
            except ValueError:
                print("Fruit price must be a number.")

    def __inputFruitQuantity__(self):
        while True:
            try:
                self.__fruitQuantity__ = int(input("Please input fruit quantity: "))
                if self.__fruitQuantity__ < 0:
                    print("Fruit quantity must be a positive value.")
                else:
                    break
            except ValueError:
                print("Fruit quantity must be a number.")

    def __inputFruitOrigin__(self):
        while True:
            self.__fruitOrigin__ = input("Please input fruit origin: ")
            if not re.fullmatch("^[\\w\\s]{3,100}$", self.__fruitOrigin__):
                print("Valid fruit origin must higher than 3 and lower than 100. Try again.")
            else:
                break

    def input(self):
        self.__inputFruitName__()
        self.__inputFruitPrice__()
        self.__inputFruitQuantity__()
        self.__inputFruitOrigin__()

    def getBasicInfo(self):
        return self.__fruitName__ + "\t\t" + self.__fruitOrigin__ + "\t\t" + str(self.__fruitPrice__)+"$"

    def __str__(self):
        return "\t" + str(self.__fruitId__) + "\t\t" + self.__fruitName__ + "\t\t" + self.__fruitOrigin__ + "\t\t" + str(self.__fruitPrice__)+"$" + "\t" + str(self.__fruitQuantity__)

    def setId(self, fruitId):
        self.__fruitId__ = fruitId

    def getId(self):
        return self.__fruitId__

    def setName(self, fruitName):
        self.__fruitName__ = fruitName

    def getName(self):
        return self.__fruitName__

    def getQuantity(self):
        return self.__fruitQuantity__

    def setQuantity(self, quantity):
        self.__fruitQuantity__ = quantity

    def getOrigin(self):
        return self.__fruitOrigin__

    def setOrigin(self, origin):
        self.__fruitOrigin__ = origin

    def setPrice(self, price):
        self.__fruitPrice__ = price

    def getPrice(self):
        return self.__fruitPrice__

    def getAmountPrice(self):
        return self.__fruitQuantity__ * self.__fruitPrice__