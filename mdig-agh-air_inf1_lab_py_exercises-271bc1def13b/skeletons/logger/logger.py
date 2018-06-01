from typing import Any


def logged(func):
    raise NotImplementedError


@logged
def foo(*args: Any) -> int:
    return len(args)


foo(1, 2, 3)
