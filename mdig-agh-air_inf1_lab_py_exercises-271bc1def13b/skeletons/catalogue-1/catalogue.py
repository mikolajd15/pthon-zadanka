from typing import Mapping
import copy

class Product:


    def __init__(self, id_: str, name: str, price: float) -> None:
        self.id=id_
        self.name=name
        self.price=price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self,value):
        if value >100:
            value=100
        self._price=value

    def __str__(self) -> str:
        return "{name} [{id}] : ${price:.2f}".format(name=self.name, id=self.id, price=self.price)


    def __eq__(self, other) -> bool:
        if (self.id==other.id) and (self.name==other.name) and (self.price==other.price):
            return True
        else:
            return False


class Catalogue:

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
            self.inventory[product.id] = copy(product)

    def get_products_with_appropriate_price(self, predicate)->dict:

        filtered = {obj.id : obj for obj in self.inventory.values() if predicate(obj.price)}

        return filtered

    def get_products_by_name_part(self, substr: str, ignore_case: bool=False)->dict:

        if ignore_case==True:
            filtered = {obj.id: obj for obj in self.inventory.values() if str.lower(substr) in str.lower(obj.name)}
        else:
            filtered = {obj.id: obj for obj in self.inventory.values() if substr in obj.name}
        return filtered