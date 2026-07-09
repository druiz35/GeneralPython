from __future__ import annotations
from abc import ABC, abstractmethod

class Abstraction:
    def __init__(self, implementation: Implementation) -> None:
        self.implementation = implementation

    def operation(self) -> str:
        return (f"Abstraction: Base operation with:\n"
                f"{self.implementation.operation_implementation()}")

class ExtendedAbstraction(Abstraction):
    def operation(self) -> str:
        return (f"ExtendedAbstraction: Extended operation with:\n"
                f"{self.implementation.operation_implementation()}")
    
    def new_method(self) -> str:
        return "this is another method of the extended abstraction"

class Implementation(ABC):
    @abstractmethod
    def operation_implementation(self) -> str:
        pass

class ConcreteImplementationA(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationA: Here's the result on the platform A"

class ConcreteImplementationB(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationB: Here's the result on the platform B"

class Client:
    def __init__(self, abstraction: str, implementation: str) -> None:
        self.abstraction: Abstraction = None
        self.implementation: Implementation = None
        self._initialize(abstraction, implementation)

    def _initialize(self, abstraction: str, implementation: str) -> None:
        # Initialize implementation
        if implementation == "A":
            self.implementation = ConcreteImplementationA()
        elif implementation == "B":
            self.implementation = ConcreteImplementationB()

        # Initialize abstractions
        if abstraction == "Base":
            self.abstraction = Abstraction(self.implementation)
        elif abstraction == "Extended":
            self.abstraction = ExtendedAbstraction(self.implementation)

if __name__ == "__main__":
    ABSTRACTION_ENV = "Extended"
    IMPLEMENTATION_ENV = "B"
    client: Client = Client(ABSTRACTION_ENV, IMPLEMENTATION_ENV)
    print(client.abstraction.operation())
    print(client.abstraction.new_method())
