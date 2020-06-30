class Person(object):

    def __init__(self):
        self.__weight__ = 0.0
        self.__height__ = 0.0

    def __inputWeight__(self):
        while True:
            try:
                if self.__weight__ <= 0.0:
                    self.__weight__ = float(input("Please input body weight (kg): "))
                else:
                    break
            except ValueError:
                print("Only accept body weight as float")

    def __inputHeight__(self):
        while True:
            try:
                if self.__height__ <= 0.0:
                    self.__height__ = float(input("Please input body height (m): "))
                else:
                    break
            except ValueError:
                print("Only accept body height as float")

    def input(self):
        self.__inputWeight__()
        self.__inputHeight__()

    def calculateBMI(self):
        return self.__weight__ / (self.__height__ * self.__height__)

    def handlingBMIIndex(self):
        BMI = self.calculateBMI()
        if BMI > 40:
            return str(BMI) + " Very fat - should lose weight immediately"
        elif BMI > 30:
            return str(BMI) + " Fat - should lose weight"
        elif BMI > 25:
            return str(BMI) + " Overweight"
        elif BMI > 19:
            return str(BMI) + " Standard"
        else:
            return str(BMI) + " Under-standard"

    def __str__(self):
        return "Height:" + str(self.__height__) + ", Weight:" + str(self.__weight__) + "\n" + self.handlingBMIIndex()
