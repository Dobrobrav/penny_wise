from typing import TypeVar, TypeAlias, Generator

T = TypeVar('T')
Generator_: TypeAlias = Generator[T, None, None]
