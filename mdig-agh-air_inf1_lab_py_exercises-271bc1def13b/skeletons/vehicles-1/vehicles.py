from typing import TypeVar, Container
from abc import ABC, abstractmethod

class Movable:
    # TODO: zaimplementuj...
    pass


class Vehicle (ABC):
    def __init__(self, id_ : str, brand : str) -> None:
        self.id=id_
        self.brand=brand

    @abstractmethod
    def max_speed(self) -> float:
        pass

    def __str__(self)->str:
        return "{id} :  {brand}".format(id=self.id , brand=self.brand)

# TODO: Zmień wywołanie TypeVar() tak, aby 'V' był podtypem klasy 'Vehicle' (zob. parametr 'bound').
V = TypeVar('V', bound = Vehicle)


def vehicle_collection_as_string(vehicles: Container[V]) -> str:

    list=''
    for v in vehicles:
        list=list+v.__str__()+'\n'

    return list.rstrip()




class Car (Vehicle):
    def __init__(self, engine_hp : float, **kwargs )->None:
        super().__init__(**kwargs)
        self.engine_hp = engine_hp

    def max_speed(self)->float:
        return self.engine_hp

class Bicycle (Vehicle):
    def __init__(self, n_gears : int, **kwargs)->None:
        super().__init__(**kwargs)
        self.n_gears=n_gears

    def max_speed(self)->int:
        return self.n_gears*3


def compute_min_travel_duration(distance: float, vehicle: Vehicle) -> float:
    return distance/vehicle.max_speed()


def compute_min_travel_duration_as_string(distance: float, vehicle: Vehicle) -> str:
    return '{duration:.3f} h'.format(duration=compute_min_travel_duration(distance,vehicle))

