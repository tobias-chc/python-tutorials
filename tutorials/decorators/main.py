"""This module demonstrates the use of decorators in Python."""

from tutorials.decorators.basics import call_twice, call_twice_safe


@call_twice
def greet_dec(name) -> None:
    """Function to greet a person."""
    print(f"Hello, {name}!")


def greet_no_dec(name) -> None:
    """Function to greet a person."""
    print(f"Hello, {name}!")


@call_twice_safe
def greet_generic(name1, name2, bye: bool = False) -> None:
    """Function to greet two people."""
    greet_str = "Hello" if not bye else "Bye"
    print(f"{greet_str}, {name1} and {name2}!")


if __name__ == "__main__":
    # Demonstrate that decorating greet_2 manually is equivalent to using @call_twice
    greet_dec_manual = call_twice(greet_no_dec)
    # assert  greet_dec_manual("Bacon") == call_twice(greet_no_dec)("Bacon")
    assert greet_dec_manual("Bacon") == greet_dec("Bacon")
    # Calls the wrapper produced by call_twice, with func = greet_no_dec
    # = wrapper("Bacon") {func=greet}

    # --- Demonstrate the proper decorator with multiple arguments and a keyword argument
    greet_generic("Bacon", "Milaneso")
    greet_generic("Bacon", "Milaneso", bye=True)

    # --- Demonstrate the effect on function metadata: @wraps decorator
    # Poor decorator (call_twice): loses original name and docstring
    assert greet_dec.__name__ == "wrapper"
    assert greet_dec.__doc__ == "Docstring for the wrapper."
    # Proper decorator (call_twice_safe): preserves original name and docstring
    assert greet_generic.__name__ == "greet_generic"
    assert greet_generic.__doc__ == "Function to greet two people."
