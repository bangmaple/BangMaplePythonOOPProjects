from CandidateManager import CandidateManager
from Experience import Experience
from Fresher import Fresher
from Internship import Internship

import os

cm = CandidateManager()


def inputChoice():
    while True:
        try:
            choice = int(input("Your choice: "))
            return choice
        except ValueError:
            print("Only accept choice as number.")


def inputExperience():
    c = Experience()
    c.input()
    print(cm.add(c))


def inputFresher():
    c = Fresher()
    c.input()
    print(cm.add(c))


def inputInternship():
    c = Internship()
    c.input()
    print(cm.add(c))


def printListCandidate():
    listExperience = cm.getAllExperience()
    listInternship = cm.getAllInternship()
    listFresher = cm.getAllFresher()
    if listExperience.__len__() > 0:
        print("===== EXPERIENCE CANDIDATE =====")
        for e in listExperience:
            print(e.getFullName())
    if listFresher.__len__() > 0:
        print("===== FRESHER CANDIDATE =====")
        for f in listFresher:
            print(f.getFullName())
    if listInternship.__len__() > 0:
        print("===== INTERNSHIP CANDIDATE =====")
        for i in listInternship:
            print(i.getFullName())


def inputCandidateName():
    return input("Input candidate name (Fist name or Last name): ")


def inputCandidateType():
    while True:
        try:
            type = int(input("Input type of candidate: "))
            if type < 0 or type > 2:
                print("Only accept candidate type from range 0-2.")
            else:
                return type
        except ValueError:
            print("Only accept candidate type as number (0-2).")


def showCandidate(res: list):
    if res.__len__() > 0:
        print("The candidates found: ")
        for i in res:
            print(i)
    else:
        print("No candidate found!")


def searching():
    printListCandidate()
    name = inputCandidateName()
    cType = inputCandidateType()
    res = cm.findRelevantCandidate(name, cType)
    showCandidate(res)


def exitProgram():
    print("Thanks for using my program.")
    os._exit(0)


def menu():
    while True:
        print("CANDIDATE MANAGEMENT SYSTEM")
        print("1. Experience")
        print("2. Fresher")
        print("3. Internship")
        print("4. Searching")
        print("5. Exit")
        print("\nChoose one...")
        choice = inputChoice()
        if choice == 1:
            inputExperience()
        elif choice == 2:
            inputFresher()
        elif choice == 3:
            inputInternship()
        elif choice == 4:
            searching()
        elif choice == 5:
            exitProgram()


if __name__ == "__main__":
    menu()
