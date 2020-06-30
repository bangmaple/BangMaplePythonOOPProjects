from Fruit import Fruit


class FruitManager(object):

    def __init__(self):
        self.__fm__ = list()

    def addFruit(self, f: Fruit):
        f.setId(len(self.__fm__) + 1)
        self.__fm__.append(f)
        return "Successfully added fruit to the store"

    def displayAll(self):
        print("List of Fruit: ")
        print("| ++ Fruit Id ++ | ++ Fruit Name ++ | ++ Fruit Origin ++ | ++ Fruit Price ++ | ++ Fruit Quantity ++")
        for i in self.__fm__:
            print(i)
        print("\n")

    def buyerViewFruits(self):
        print("List of Fruit:")
        print("| ++ Item ++ | ++ Fruit Name ++ | ++ Origin ++ | ++ Price ++ |")
        counter = 1
        for i in self.__fm__:
            print("\t" + str(counter) + "\t\t" + i.getBasicInfo())
            counter = counter + 1

    def getFruitByName(self, fruitName: str):
        for i in self.__fm__:
            if i.getName().lower().strip() == fruitName.lower().strip():
                if i.getQuantity() < 1:
                    return None
                else:
                    return i
        return None

    def getAllFruitQuantity(self):
        return len(self.__fm__)