from Cart import Cart
from Fruit import Fruit
from FruitManager import FruitManager
from Cart import Cart
from Order import Order
import os

fm = FruitManager()
order = Order()


def choiceMenu():
    while True:
        try:
            choice = int(input("Please choose: "))
            if choice < 1 or choice > 4:
                print("Only accept input range from 1-4. Try again.")
            else:
                return choice
        except ValueError:
            print("Only accept input as number. Try again.")


def exit():
    print("Thanks for using my program.")
    os._exit(0)


def createFruit():
    while True:
        f = Fruit()
        f.input()
        print(fm.addFruit(f))
        choice = input("Do you want to continue? (Y/N): ")
        if choice == "N" or choice == "n":
            fm.displayAll()
            break


def viewOrders():
    print("view orer")
    order.displayAll()


def getFruitQuantity(f: Fruit):
    while True:
        try:
            quantity = int(input("Please input quantity: "))
            if quantity < 0 or quantity > f.getQuantity():
                print("The input quantity must be lower than 0 or higher than the stock. Please try again.")
            else:
                return quantity
        except ValueError:
            print("Only accept fruit quantity as number.")


def shopping():
    if fm.getAllFruitQuantity() > 0:
        while True:
            fm.buyerViewFruits()
            fruitName = input("Please select fruit name (select '*' to exit): ").strip()
            if fruitName == "*":
                break
            f: Fruit = fm.getFruitByName(fruitName)
            if f is None:
                print("\nThe fruit name you want to select does not exist or out of stock. Please try again.\n")
                continue
            print("You selected: " + fruitName)

            quantity = getFruitQuantity(f)
            f.setQuantity(f.getQuantity() - quantity)
            ff = Fruit()
            ff.setId(f.getId())
            ff.setName(f.getName())
            ff.setOrigin(f.getOrigin())
            ff.setQuantity(quantity)
            ff.setPrice(f.getPrice())

            c = Cart()
            c.addFruitToCart(ff)
            name = input("Input your name: ")
            order.addToOrder(name, c)
            print("Successfully added to your order.")
            choice = input("Do you want to continue ordering? (Y/N): ")
            if choice == "N" or choice == "n":
                break
    else:
        print("\nThis fruit store is out of stock. Please come back later.\n")


def menu():
    while True:
        print("FRUIT SHOP SYSTEM")
        print("1. Create Fruit")
        print("2. View orders")
        print("3. Shopping (for buyer)")
        print("4. Exit")
        choice = choiceMenu()
        if choice == 1:
            createFruit()
        elif choice == 2:
            viewOrders()
        elif choice == 3:
            shopping()
        else:
            exit()


if __name__ == "__main__":
    menu()