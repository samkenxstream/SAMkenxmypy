# NOTE: Requires fixtures/dict.pyi
from typing import (
    Any, Dict, Type, TypeVar, Optional, Any, Generic, Mapping, NoReturn as NoReturn, Iterator,
    Union
)
import sys

_T = TypeVar('_T')
_U = TypeVar('_U')


def Arg(type: _T = ..., name: Optional[str] = ...) -> _T: ...

def DefaultArg(type: _T = ..., name: Optional[str] = ...) -> _T: ...

def NamedArg(type: _T = ..., name: Optional[str] = ...) -> _T: ...

def DefaultNamedArg(type: _T = ..., name: Optional[str] = ...) -> _T: ...

def VarArg(type: _T = ...) -> _T: ...

def KwArg(type: _T = ...) -> _T: ...


# Fallback type for all typed dicts (does not exist at runtime).
class _TypedDict(Mapping[str, object]):
    # Needed to make this class non-abstract. It is explicitly declared abstract in
    # typeshed, but we don't want to import abc here, as it would slow down the tests.
    def __iter__(self) -> Iterator[str]: ...
    def copy(self: _T) -> _T: ...
    # Using NoReturn so that only calls using the plugin hook can go through.
    def setdefault(self, k: NoReturn, default: object) -> object: ...
    # Mypy expects that 'default' has a type variable type.
    def pop(self, k: NoReturn, default: _T = ...) -> object: ...
    def update(self: _T, __m: _T) -> None: ...
    if sys.version_info < (3, 0):
        def has_key(self, k: str) -> bool: ...
    def __delitem__(self, k: NoReturn) -> None: ...

def TypedDict(typename: str, fields: Dict[str, Type[_T]], *, total: Any = ...) -> Type[dict]: ...

# This is intended as a class decorator, but mypy rejects abstract classes
# when a Type[_T] is expected, so we can't give it the type we want.
def trait(cls: Any) -> Any: ...

# The real type is in the comment but it isn't safe to use **kwargs in
# a lib-stub because the fixtures might not have dict. Argh!
# def mypyc_attr(*attrs: str, **kwattrs: object) -> Callable[[_T], _T]: ...
mypyc_attr: Any

class FlexibleAlias(Generic[_T, _U]): ...

if sys.version_info >= (3, 0):
    _Int = Union[int, i32, i64]

    class i32:
        def __init__(self, x: _Int) -> None: ...
        def __add__(self, x: i32) -> i32: ...
        def __radd__(self, x: i32) -> i32: ...
        def __lt__(self, x: i32) -> bool: ...
        def __neg__(self) -> i32: ...
        def __invert__(self) -> i32: ...
        def __pos__(self) -> i32: ...
        def __floordiv__(self, x: i32) -> i32: ...
        def __mod__(self, x: i32) -> i32: ...

    class i64:
        def __init__(self, x: _Int) -> None: ...
        def __add__(self, x: i64) -> i64: ...
        def __radd__(self, x: i64) -> i64: ...
        def __sub__(self, x: i64) -> i64: ...
        def __rsub__(self, x: i64) -> i64: ...
        def __mul__(self, x: i64) -> i64: ...
        def __rmul__(self, x: i64) -> i64: ...
        def __floordiv__(self, x: i64) -> i64: ...
        def __rfloordiv__(self, x: i64) -> i64: ...
        def __mod__(self, x: i64) -> i64: ...
        def __rmod__(self, x: i64) -> i64: ...
        def __and__(self, x: i64) -> i64: ...
        def __rand__(self, x: i64) -> i64: ...
        def __or__(self, x: i64) -> i64: ...
        def __ror__(self, x: i64) -> i64: ...
        def __xor__(self, x: i64) -> i64: ...
        def __rxor__(self, x: i64) -> i64: ...
        def __lshift__(self, x: i64) -> i64: ...
        def __rlshift__(self, x: i64) -> i64: ...
        def __rshift__(self, x: i64) -> i64: ...
        def __rrshift__(self, x: i64) -> i64: ...
        def __neg__(self) -> i64: ...
        def __invert__(self) -> i64: ...
        def __lt__(self, x: i64) -> bool: ...
        def __le__(self, x: i64) -> bool: ...
        def __ge__(self, x: i64) -> bool: ...
        def __gt__(self, x: i64) -> bool: ...
