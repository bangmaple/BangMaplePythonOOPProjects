from Candidate import Candidate


class Fresher(Candidate):

    def __init__(self):
        super().__init__()
        self.__graduationDate__ = 0
        self.__graduationRank__ = ""
        self.__education__ = ""
        self.__type__ = 1

    def __inputGraduationDate__(self):
        while True:
            try:
                self.__graduationDate__ = int(input("Please input graduation date as year: "))
                if self.__graduationDate__ > 2020 or self.__graduationDate__ < 1900:
                    print("Not a valid graduation date. Try again.")
                else:
                    break
            except ValueError:
                print("Only accept graduation date as valid year.")

    def __inputGraduationRank__(self):
        rankOfGraduation = ["Excellent", "Good", "Fair", "Poor"]
        while True:
            self.__graduationRank__ = input("Please input graduation rank: ")
            if self.__graduationRank__ in rankOfGraduation:
                break
            else:
                print("Only accept one of the following rank: Excellent, Good, Fair, Poor. Try again.")

    def __inputEducation__(self):
        self.__education__ = input("Please input the education place: ")

    def input(self):
        super().input()
        self.__inputGraduationDate__()
        self.__inputGraduationRank__()
        self.__inputEducation__()
