from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any

class CustomIterator(Iterator):
    _position: int = None
    _custom_behavior: bool = False

    def __init__(self, collection: CustomCollection, custom_behavior: bool = False) -> None:
        self._collection = collection
        self._custom_behavior = custom_behavior
        self._custom_items = None
        self._position = 0

    def __next__(self) -> Any:
        if self._custom_items is None:
            self._custom_items = sorted(self._collection._collection)
            if self._custom_behavior:
                self._custom_items = list(reversed(self._custom_items))

        if self._position >= len(self._custom_items):
            raise StopIteration()

        value = self._custom_items[self._position]
        self._position += 1
        return value

class CustomCollection(Iterable):
    def __init__(self, collection: list[Any] | None = None) -> None:
        self._collection = collection or []

    def __getitem__(self, index: int) -> Any:
        return self._collection[index]

    def __iter__(self) -> AlphabeticalOrderIterator:
        return CustomIterator(self)

    def reversed(self) -> AlphabeticalOrderIterator:
        return CustomIterator(self, True)
    
    def add(self, item: Any) -> None:
        self._collection.append(item)

if __name__ == "__main__":
    collection = CustomCollection()
    collection.add("B")
    collection.add("A")
    collection.add("C")

    print("".join(collection))
    print("".join(collection.reversed()))
    print(collection[1])

    for item in collection:
        print(item)
