from box import ConfigBox
from typing import Any, Callable
import inspect

class Utility:
    @staticmethod
    def ensure_annotation(func: Callable) -> Callable:
        """
        Décorateur pour vérifier que les arguments d'une fonction 
        respectent leurs annotations de type.
        """
        def wrapper(*args, **kwargs) -> Any:
            sig = inspect.signature(func)
            for param, arg in zip(sig.parameters.values(), args):
                if param.annotation != inspect.Parameter.empty and not isinstance(arg, param.annotation):
                    raise TypeError(f"L'argument {param.name} doit être de type {param.annotation}, mais a reçu {type(arg)}.")
            return func(*args, **kwargs)
        return wrapper
