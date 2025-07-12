"""Basics decorator examples"""

from functools import wraps
from typing import Any, Callable


# Poor decorator (does not preserve metadata) and dows not take multiple arguments
def call_twice(func: Callable) -> Callable:
    """Decorator that calls the function twice."""

    def wrapper(one_arg) -> Any:
        """Docstring for the wrapper."""
        func(one_arg)
        func(one_arg)

    return wrapper


# Proper decorator that preserves metadata and can take multiple arguments
def call_twice_safe(func: Callable) -> Callable:
    """Decorator that calls the function twice."""

    @wraps(func)
    def call_twice_safe_wraper(*args, **kwargs) -> Any:
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return call_twice_safe_wraper
