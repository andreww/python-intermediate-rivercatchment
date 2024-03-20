def plus(a: int, b: int) -> int:
    return a+b


def greet(who: str) -> None:
    print("Hi" + who)


def greetNum(who: tuple[str, int]) -> None:
    print(who[0] * who[1])


greet("a")
greetNum(("Andrew", 2))

