from typing import List, Any, Union, Sequence, Callable, Collection, MutableSequence, Mapping, TypeVar


def list_print() -> None:
    """Wypisz poniższą listę w formacie:
        0  ->  red
        1  ->  green
        2  ->  blue
    Skorzystaj z funkcji enumerate().
    """
    colors = ['red', 'green', 'blue']
    raise NotImplementedError


def remove_duplicates(elements: Collection[Any]) -> List[Any]:
    """Usuń duplikaty z listy (bez zachowania kolejności).
    Skorzystaj z funkcji list() i set().

    Przykład: [1, 1, 2, 2] -> [2, 1]

    Parametry:
    elements -- lista elementów, z której należy usunąć duplikaty
    """
    raise NotImplementedError


# TODO: zastąp poniższą linijkę definicją nazwanej krotki (namedtuple) MinMax o polach 'min' i 'max'
MinMax = TypeVar('MinMax')

Num = Union[int, float]


def min_max(numbers: Sequence[Num], upper_limit: Num = None) -> MinMax:
    """Zwróć najmniejszą i największą spośród liczb przekazanych w kolekcji `numbers`.
    Jeśli największa przekazana liczba jest większa niż organiczenie górne, zwróć ograniczenie.

    Parametry:
    numbers -- kolekcja liczb
    upper_limit -- maksymalna wartość największej liczby

    Typ zwracany: namedtuple (pola: min, max)
    """
    raise NotImplementedError


def append(elements: MutableSequence[Any] = None) -> MutableSequence[Any]:
    """Dodaj "hi" na koniec listy.
    Wywołanie z argumentem domyślnym powinno zwrócić listę ["hi"].
    Skorzystaj z metody append().

    elements -- lista, do której dopisujemy
    """
    raise NotImplementedError


def sum_values(my_dict: Mapping[Any, Num]) -> Num:
    """Posumuj wszystkie wartości w słowniku.
    Wykorzystaj metodę values().

    Parametry:
    my_dict -- słownik, którego wartości są sumowane
    """
    raise NotImplementedError


def filter_pesels_by_name_initial(persons: Mapping[str, str], name_initial: str) -> List[str]:
    """Zwróć zbiór PESEL-i osób, których imię zaczyna się zadaną literę.
    Aby zwrócić pożądany zbiór, utwórz w funkcji nową listę.

    Parametry:
    persons -- baza osób {PESEL -> osoba}
    name_initial -- inicjał imienia użyty do filtrowania
    """
    raise NotImplementedError


def repeat(f: Callable[[Num], Num]) -> List[Num]:
    """Zwróć listę wartości zwróconych przez wywołanie f()
    z argumentami 1, 3 i 5.

    Parametry:
    f -- jednoargumentowa funkcja przyjmująca i zwracająca liczbę
    """
    raise NotImplementedError


def count_if(words: Sequence[str]) -> int:
    """Zwróć liczbę słów z listy spełniających oba poniższe warunki:
    - długość słowa wynosi co najmniej 2
    - słowo zaczyna się na litetę 'a' lub jest palindromem
    """
    raise NotImplementedError


def mul_if(numbers: Sequence[Num], predicate: Callable[[Num], bool]) -> Num:
    """Zwróć iloczyn liczb spełniających predykat.
    Skorzystaj z funkcji filter(), reduce(), oraz operator.mul().

     Parametry:
     numbers -- kolekcja liczb
     predicate -- predykat
    """
    raise NotImplementedError
