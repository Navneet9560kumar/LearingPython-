class BaseChai:
    def __init__(self, type_):      # ✅ Parameter name fixed
        self.type = type_

    def prepare(self):              # ✅ Method is now outside __init__
        print(f"Preparing {self.type} chai....")


class MasalaChai(BaseChai):
    def add_spices(self):
        print("Adding cardamom, ginger, clove.")


class chaiShop:
    chai_cls = BaseChai  # ✅ Not an object, but the class itself

    def __init__(self):
        self.chai = self.chai_cls("Regular")  # ✅ Dynamic class calling

    def server(self):
        print(f"Serving {self.chai.type} chai in the shop")
        self.chai.prepare()


class FancyChaiShop(chaiShop):
    chai_cls = MasalaChai  # ✅ Overriding chai_cls with MasalaChai class


# ✅ Creating objects
shop = chaiShop()
fancy = FancyChaiShop()

# ✅ Calling method
fancy.server()

# ✅ Calling spice method
fancy.chai.add_spices()
