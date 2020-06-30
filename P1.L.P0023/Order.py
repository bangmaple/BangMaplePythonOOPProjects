from Cart import Cart


class Order(object):
    def __init__(self):
        self.__ord__ = dict()

    def addToOrder(self, name: str, c: Cart):
        if len(self.__ord__) < 1:
            self.__ord__.update({name: c})
        else:
            flag = False
            for i in self.__ord__.items():
                if i[0] == name:
                    flag = True
                    for j in c.getCart():
                        i[1].addFruitToCart(j)
            if flag is False:
                self.__ord__.update({name: c})

    def displayAll(self):
        print(len(self.__ord__))
        for i in self.__ord__:
            print("\nCustomer: " + i)
            self.__ord__[i].displayAll()
