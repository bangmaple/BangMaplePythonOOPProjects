from Person import Person
from Math import Math
import os


def calculator():
    m = Math()
    res = m.input()
    print("The result: " + res)


def calBMI():
    p = Person()
    p.input()
    print(p)


def menu():
    print("Please choose an option!")
    print("1. Normal Calculator")
    print("2. Calculate BMI Index")
    print("3. Exit")
    try:
        choice = int(input("\nChoose one: "))
        if choice == 1:
            calculator()
        elif choice == 2:
            calBMI()
        else:
            print("Thanks for using my program.")
            os._exit(0)
    except ValueError:
        print("Only accept input as number.")


if __name__ == "__main__":
    while True:
        menu()
        prompt = input("Do you want to continue (Y/N)? ")
        if prompt == "N" or prompt == "n":
            break
