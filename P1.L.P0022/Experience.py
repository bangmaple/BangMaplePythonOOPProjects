from Candidate import Candidate


class Experience(Candidate):

    def __init__(self):
        super().__init__()
        self.__expInYear__ = -1
        self.__proSkill__ = ""
        self.__type__ = 0

    def __inputExpInYear__(self):
        while True:
            try:
                self.__expInYear__ = int(input("Please input experience in year: "))
                if self.__expInYear__ < 0 or self.__expInYear__ > 100:
                    print("Experience in year must higher than 0 and lower than 100. Try again.")
                else:
                    break
            except ValueError:
                print("Only accept experience in year as positive number.")

    def __inputProSkill__(self):
        self.__proSkill__ = input("Please input your professional skill: ")

    def hihi(self):
        print("hisdsd")

    def input(self):
        super().input()
        self.__inputExpInYear__()
        self.__inputProSkill__()