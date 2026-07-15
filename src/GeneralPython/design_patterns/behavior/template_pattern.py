from abc import ABC, abstractmethod

class AbstractClass(ABC):
    def template_method(self) -> None:
        self.bo1()
        self.ro1()
        self.bo2()
        self.h1()
        self.ro2()
        self.bo3()
        self.h2()

    def bo1(self) -> None:
        print("AbstractClass: Doing Base Op 1")

    def bo2(self) -> None:
        print("AbstractClass: Doing Base Op 2")

    def bo3(self) -> None:
        print("AbstractClass: Doing Base Op 3")

    @abstractmethod
    def ro1(self) -> None:
        pass

    @abstractmethod
    def ro2(self) -> None:
        pass

    def h1(self) -> None:
        pass

    def h2(self) -> None:
        pass

class ConcreteClass1(AbstractClass):
    def ro1(self) -> None:
        print("CC1: Implemented Required Op 1")

    def ro2(self) -> None:
        print("CC1: Implemented Required Op 2")

class ConcreteClass2(AbstractClass):
    def ro1(self) -> None:
        print("CC2: Implemented Required Op 1")

    def ro2(self) -> None:
        print("CC2: Implemented Required Op 2")

    def h2(self) -> None:
        print("CC2: Overriden Hook 2")

def client_code(ass: AbstractClass) -> None:
    ass.template_method()

if __name__ == "__main__":
    client_code(ConcreteClass1())
    print()
    client_code(ConcreteClass2())
