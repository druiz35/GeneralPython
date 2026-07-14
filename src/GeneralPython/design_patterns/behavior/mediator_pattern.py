from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class Mediator(ABC):
    @abstractmethod
    def notify(self, sender: Any, event: str) -> str:
        pass

class ConcreteMediator(Mediator):
    def __init__(self, componentA: Any, componentB: Any):
        self._componentA = componentA
        self._componentA.mediator = self
        self._componentB = componentB
        self._componentB.mediator = self

    def notify(self, event: Any) -> str:
        if event == "A":
            print("Reacting on A (A.do_stuff)")
            self._componentA.do_stuff()
        elif event == "B":
            print("Reacting on B (B.do_stuff, A.do_other_stuff, A.do_stuff")
            self._componentB.do_stuff()
            self._componentA.do_other_stuff()
            self._componentA.do_stuff()

class BaseComponent:
    def __init__(self, mediator: Mediator = None) -> None:
        self._mediator = mediator

    @property
    def mediator(self) -> Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator) -> None:
        self._mediator = mediator

class ComponentA(BaseComponent):
    def do_stuff(self) -> str:
        print("I'm A and I'm doing stuff")

    def do_other_stuff(self) -> str:
        print("I'm A and I'm doing other stuff")

class ComponentB(BaseComponent):
    def do_stuff(self) -> str:
        print("I'm B and I'm doing stuff")

if __name__ == "__main__":
    componentA = ComponentA()
    componentB = ComponentB()
    mediator = ConcreteMediator(componentA, componentB)
    mediator.notify("A")
    print("")
    mediator.notify("B")
