from typing import Mapping
import copy

class Product:
    # TODO: zaimplementuj...

    def __init__(self, id_: str, name: str, price: float) -> None:
        self.id=id_
        self.name=name
        self.price=price


    def __str__(self) -> str:
        return "{name} [{id}] : ${price:.2f}".format(name=self.name, id=self.id, price=self.price)


    def __eq__(self, other) -> bool:
        if (self.id==other.id) and (self.name==other.name) and (self.price==other.price):
            return True
        else:
            return False


class Catalogue:
    # TODO: zaimplementuj...

    Inventory = Mapping[str, Product]

    def __init__(self, inventory:Inventory=None )->None:
        self.inventory=copy.deepcopy(inventory)

    def __contains__(self, id_: str) -> bool:
        if (self.inventory==None) or (id_ not in self.inventory):
            return False
        else:
            return True

    def add_product(self, product: Product)->None:
        if(self.inventory==None):
            self.inventory={product.id : product}
        else:
            self.inventory[product.id] = product
