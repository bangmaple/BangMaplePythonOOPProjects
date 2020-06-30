from Candidate import Candidate


class Internship(Candidate):

    def __init__(self):
        super().__init__()
        self.__major__ = ""
        self.__semester__ = 0
        self.__universityName__ = ""
        self.__type__ = 2

    def __inputMajor__(self):
        self.__major__ = input("Please input major: ")

    def __inputSemester__(self):
        while True:
            try:
                self.__semester__ = int(input("Please input semester: "))
                if self.__semester__ < 1 or self.__semester__ > 9:
                    print("Only accept semester in range 1-9. Try again.")
                else:
                    break
            except ValueError:
                print("Only accept semester as number.")

    def __inputUniversityName__(self):
        self.__universityName__ = input("Please input university name: ")

    def input(self):
        super().input()
        self.__inputMajor__()
        self.__inputSemester__()
        self.__inputUniversityName__()