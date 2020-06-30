from Fruit import Fruit


class Cart(object):

    def __init__(self):
        self.__c__ = list()

    def addFruitToCart(self, f: Fruit):
        flag = False
        if len(self.__c__) > 0:
            for i in self.__c__:
                if f.getId() == i.getId():
                    i.setQuantity(i.getQuantity() + f.getQuantity())
                    flag = True
        if flag is False:
            self.__c__.append(f)

    def displayAll(self):
        counter = 1
        total = 0
        print("Product | Quantity | Price | Amount")
        for i in self.__c__:
            print(str(counter) + "." + i.getName() + "\t" + str(i.getQuantity()) + "\t" + str(i.getPrice()) + "$\t" + str(i.getAmountPrice())+"$")
            total = total + i.getAmountPrice()
            counter = counter + 1
        print("Total: " + str(total) + "$\n")

    def getCart(self):
        return self.__c__