import sys
import os

from decorator import *


class Menu:
    def __init__(self):
        self.items = list()

    def add_item(self, text, function):
        self.items.append({'text': text, 'func': function})

    def show(self):
        i = 1
        for element in self.items:
            print("{}. {}".format(i, element['text']))
            i += 1
        print("\n")

    def do(self, i):
        return self.items[i]['func']


def end(burger):
    print(burger)
    print("-----------------------------------")
    print("TOTAL: %.2f €" % burger.total())
    exit()


def exit():
    sys.exit(0)


def menu_burger(burger=None):
    menu1 = Menu()
    menu1.add_item("CheeseBurger", CheeseBurger)
    menu1.add_item("FishBurger", FishBurger)
    menu1.add_item("Exit", exit)

    os.system('clear')
    print("!!! Welcome to Jonh's Burger !!!\n\n")
    print("Choice your burger:")
    menu1.show()
    i = int(input(">>> "))
    os.system('clear')
    burger_name = menu1.do(i-1)
    if burger_name != exit:
        sauce = input("What sauce?? ")
        burger = burger_name(sauce)
    else:
        exit()
    return burger


def menu_supp(burger):
    menu2 = Menu()
    menu2.add_item("Tomato", Tomato)
    menu2.add_item("Salad", Salad)
    menu2.add_item("Oinon", Oinon)
    menu2.add_item("Fries", Fries)
    menu2.add_item("END", end)
    menu2.add_item("Exit", exit)

    menu2.show()
    i = int(input(">>> "))
    os.system('clear')
    supp_name = menu2.do(i-1)
    if supp_name != exit:
        burger = supp_name(burger)
    else:
        exit()
    return burger


if __name__ == "__main__":
    burger = None
    while(True):
        if burger is None:
            burger = menu_burger(burger)
        else:
            print(burger)
            burger = menu_supp(burger)
