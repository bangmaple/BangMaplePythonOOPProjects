import re
from datetime import date


class Candidate(object):
    def __init__(self):
        self.__id__ = ""
        self.__firstName__ = ""
        self.__lastName__ = ""
        self.__birthDate__ = ""
        self.__address__ = ""
        self.__phone__ = ""
        self.__email__ = ""
        self.__type__ = -1

    def __inputFirstName__(self):
        while True:
            self.__firstName__ = input("Please input candidate first name: ")
            if not re.match("^[A-Za-z\\s]{2,100}$", self.__firstName__):
                print("Only accept valid candidate first name length higher than 2 and below 100. Try again.")
            else:
                break

    def __inputLastName__(self):
        while True:
            self.__lastName__ = input("Please input candidate last name: ")
            if not re.match("^[A-Za-z\\s]{2,100}$", self.__lastName__):
                print("Only accept valid candidate last name length higher than 2 and below 100. Try again.")
            else:
                break

    def getFullName(self):
        return self.__firstName__ + " " + self.__lastName__

    def getType(self):
        return self.__type__

    def __inputBirthDate__(self):
        while True:
            self.__birthDate__ = input("Please input candidate birth date (dd/MM/yyyy): ")
            getDate = self.__birthDate__.split("/")
            try:
                date(int(getDate[2]), int(getDate[1]), int(getDate[0]))
                break
            except ValueError:
                print("The date you input did not valid. Please try again.")

    def __inputAddress__(self):
        while True:
            self.__address__ = input("Please input candidate address: ")
            if self.__address__.__len__() > 200:
                print("Only accept address length below 200. Try again.")
            else:
                break

    def __inputPhone__(self):
        while True:
            self.__phone__ = input("Please input candidate phone: ")
            if not re.match("^[0-9]{10,}$", self.__phone__):
                print("Only accept candidate phone number has a minimum of 10-digit.")
            else:
                break

    def __inputEmail__(self):
        while True:
            self.__email__ = input("Please input candidate email: ").lower()
            if not re.match("^[a-z0-9_.]{5,32}@[a-z0-9]{2,}(.[a-z0-9]{2,4}){1,2}$", self.__email__):
                print("Only accept valid candidate email.")
            else:
                break

    def input(self):
        self.__inputFirstName__()
        self.__inputLastName__()
        self.__inputBirthDate__()
        self.__inputAddress__()
        self.__inputPhone__()
        self.__inputEmail__()

    def __str__(self):
        return self.getFullName() + " | " + self.__birthDate__ + " | " + self.__address__ + " | " + self.__phone__ + " | " + self.__email__ + " | " + str(self.__type__)