def re_word() -> str:
    """Dopasowanie: ciąg "al" w dowolnym miejscu łańcucha
    """
    raise NotImplementedError


def re_begin() -> str:
    """Dopasowanie: ciąg "al" na początku łańcucha
    """
    raise NotImplementedError


def re_end() -> str:
    """Dopasowanie: ciąg "st" na końcu łańcucha
    """
    raise NotImplementedError


def re_wildchar() -> str:
    """Dopasowanie: wszystkie znaki począwszy od '=' do końca linii
    """
    raise NotImplementedError


def re_n_alnums() -> str:
    """Dopasowanie: ciąg (dokładnie) czterech znaków alfanumerycznych
    """
    raise NotImplementedError


def re_binary() -> str:
    """Dopasowanie: ciąg składający się z cyfr 0 lub 1 (dowolnej długości)
    """
    raise NotImplementedError


def re_mobile() -> str:
    """Dopasowanie: numer telefonu komórkowego

    Uwagi:
     - opcjonalny numer kierunkowy: 2 bądź 3 cyfry poprzedzone znakiem '+'
     - między numerem kierunkowym a "głównym" numerem może znajdować się
       dowolna liczba spacji
     - "główny" numer to ciąg 9 cyfr (bez żadnych znaków rozdzielających)
    """
    raise NotImplementedError
