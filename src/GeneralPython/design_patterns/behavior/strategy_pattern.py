from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Context:
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self):
        return self._strategy
    
    @strategy.setter
    def strategy(self, strategy: Strategy):
        self._strategy = strategy

    def do_stuff(self) -> None:
        print("Context: Doing stuff")
        result = self._strategy.do_algo(data=["A", "B", "C", "D", "E"])
        print(",".join(result))

class Strategy(ABC):
    @abstractmethod
    def do_algo(self, data: List) -> List:
        pass

class StrategyA(Strategy):
    def do_algo(self, data: List) -> List:
        return sorted(data)

class StrategyB(Strategy):
    def do_algo(self, data: List) -> List:
        return reversed(sorted(data))

if __name__ == "__main__":
    context = Context(StrategyA())
    context.do_stuff()
    print()

    context.strategy = StrategyB()
    context.do_stuff()
