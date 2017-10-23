class Burger:
    def __init__(self, name, sauce):
        self.name = name
        self.sauce = sauce
        self.element = ["Breads"]

    def __repr__(self):
        return "{} sauce {}".format(self.name, self.sauce)


class CheeseBurger(Burger):
    def __init__(self, sauce):
        super().__init__("CheeseBurger", sauce)
        self.element.append("Cheese")
        self.element.append("Beef")
        self.element.append(sauce)


class FishBurger(Burger):
    def __init__(self, sauce):
        super().__init__("FishBurger", sauce)
        self.element.append("Fish")
        self.element.append(sauce)


class BurgerDecorator(Burger):
    def __init__(self, burger, supp):
        super().__init__(burger.name, burger.sauce)
        self.burger = burger
        self.supp = supp
        self.element = burger.element

    def __repr__(self):
        string = repr(self.burger)
        if self.supp not in string:
            string += ", supplement {}".format(self.supp)
        return string


class Tomato(BurgerDecorator):
    def __init__(self, burger):
        self.supp = "tomato"
        super().__init__(burger, self.supp)
        self.burger.element.append(self.supp)


class Salade(BurgerDecorator):
    def __init__(self, burger):
        self.supp = "salad"
        super().__init__(burger, self.supp)
        self.burger.element.append(self.supp)
