from typing import Dict, List
from __future__ import annotations
import json

class Flyweight:
    def __init__(self, shared_state: str) -> None:
        self._shared_state = shared_state

    def operation(self, unique_state: str) -> None:
        s = json.dumps(self._shared_state)
        u = json.dumps(unique_state)
        print(f"Shared state: {s}\n Unique state: {u}\n")

class FlyweightFactory:
    _flyweights: Dict[str, Flyweight] = {}

    def __init__(self, initial_flyweights: Dict) -> None:
        for state in initial_flyweights:
            self._flyweights[self.get_key(state)] = Flyweight(state)

    def get_key(self, state: Dict) -> str:
        return "_".join(sorted(state))

    def get_flyweight(self, shared_state: Dict) -> Flyweight:
        key = self.get_key(shared_state)
        if not self._flyweights.get(key):
            print("Factory: Can't find flyweight. Creating new one")
            self._flyweights[key] = Flyweight(shared_state)
        else:
            print("Factory: Reusing existing flyweight.")
        return self._flyweights[key]

    def list_flyweights(self) -> None:
        count = len(self._flyweights)
        print(f"Factory: There are {count} flyweights")
        print("\n".join(map(str, self._flyweights.keys())))

def add_flyweight(
        factory: FlyweightFactory, 
)
