class Burger:
    def __init__(self, name, sauce):
        self.name = name
        self.sauce = sauce
        self.element = list()

    def __repr__(self):
        return "{} sauce {}".format(self.name, self.sauce)

    def total(self):
        return sum(elem[1] for elem in self.element)


class CheeseBurger(Burger):
    def __init__(self, sauce):
        self.name = "CheeseBurger"
        super().__init__(self.name, sauce)
        self.element.append(("Bread", 1.00))
        self.element.append(("Cheese", 0.5))
        self.element.append(("Beef", 1.00))
        self.element.append((sauce, 0.5))


class FishBurger(Burger):
    def __init__(self, sauce):
        self.name = "FishBurger"
        super().__init__(self.name, sauce)
        self.element.append(("Bread", 1.00))
        self.element.append(("Fish", 1.50))
        self.element.append((sauce, 0.5))


class BurgerDecorator(Burger):
    def __init__(self, burger, supp):
        super().__init__(burger.name, burger.sauce)
        self.burger = burger
        self.supp = supp
        self.element = burger.element

    def __repr__(self):
        string = repr(self.burger)
        if "with" not in string:
            string += " with "
        if self.supp not in string:
            string += "{} ".format(self.supp)
        return string


class Tomato(BurgerDecorator):
    def __init__(self, burger):
        self.supp = "tomato"
        super().__init__(burger, self.supp)
        self.burger.element.append((self.supp, 0.2))


class Salad(BurgerDecorator):
    def __init__(self, burger):
        self.supp = "salad"
        super().__init__(burger, self.supp)
        self.burger.element.append((self.supp, 0.2))


class Oinon(BurgerDecorator):
    def __init__(self, burger):
        self.supp = "oinon"
        super().__init__(burger, self.supp)
        self.burger.element.append((self.supp, 0.2))


class Fries(BurgerDecorator):
    def __init__(self, burger):
        self.supp = "fries"
        super().__init__(burger, self.supp)
        self.burger.element.append((self.supp, 0.4))


if __name__ == '__main__':
    cheese_burger = CheeseBurger("Ketchup")
    print(cheese_burger)
    cheese_burger_with_tomato = Tomato(cheese_burger)
    print(cheese_burger_with_tomato)
    fish_burger = Fries(Tomato(Salad(FishBurger("Tartar"))))
    print(fish_burger)
