
version = "1.0.0"
print(f"Welcome to mypackage version {version}")
from . import module1
from . import module2
__all__ = ["module1", "module2"]
