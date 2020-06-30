class Math(object):
    def __init__(self):
        __num1__ = 0
        __num2__ = 0

    def __inputNum1__(self):
        while True:
            try:
                self.__num1__ = float(input("Please input number 1: "))
                break
            except ValueError:
                print("Must be number.")

    def __inputNum2__(self):
        while True:
            try:
                self.__num2__ = float(input("Please input number 1: "))
                break
            except ValueError:
                print("Must be number.")

    def __inputOp__(self):
        op = input("Please input operator (+, -, *, /, ^): ")
        if op == "+":
            return self.__getSum__()
        elif op == "-":
            return self.__getAbstract__()
        elif op == "*":
            return self.__getMul__()
        elif op == "/":
            return self.__getDivide__()
        elif op == "^":
            return self.__getMu__()

    def input(self):
        self.__inputNum1__()
        self.__inputNum2__()
        return self.__inputOp__()

    def __getSum__(self):
        return str(self.__num1__ + self.__num2__)

    def __getAbstract__(self):
        return str(self.__num1__ - self.__num2__)

    def __getDivide__(self):
        return str(self.__num1__ / self.__num2__)

    def __getMul__(self):
        return str(self.__num1__ * self.__num2__)

    def __getMu__(self):
        return str(self.__num1__ ** self.__num2__)