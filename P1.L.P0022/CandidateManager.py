from Candidate import Candidate
from Experience import Experience
from Internship import Internship
from Fresher import Fresher
import re


class CandidateManager(object):

    def __init__(self):
        self.__cm__ = list()

    def add(self, c: Candidate):
        self.__cm__.append(c)
        return "Successfully added a candidate"

    # noinspection PyMethodMayBeStatic
    def __isExperience__(self, c: Candidate):
        if isinstance(c, Experience):
            return True
        else:
            return False

    # noinspection PyMethodMayBeStatic
    def __isInternship__(self, c: Candidate):
        if isinstance(c, Internship):
            return True
        else:
            return False

    # noinspection PyMethodMayBeStatic
    def __isFresher__(self, c: Candidate):
        if isinstance(c, Fresher):
            return True
        else:
            return False

    def getAllExperience(self):
        return list(filter(self.__isExperience__, self.__cm__))

    def getAllFresher(self):
        return list(filter(self.__isFresher__, self.__cm__))

    def getAllInternship(self):
        return list(filter(self.__isInternship__, self.__cm__))

    def findRelevantCandidate(self, name: str, cType: int):
        tmpList = list()
        for i in self.__cm__:
            if re.match(name, i.getFullName().lower().lstrip().rstrip().strip()) and i.getType() == cType:
                tmpList.append(i)
        return tmpList
