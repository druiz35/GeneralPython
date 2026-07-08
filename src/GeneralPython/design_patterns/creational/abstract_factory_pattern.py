from abc import ABC, abstractmethod
import os


class ProductA(ABC):
    @abstractmethod
    def do_something(self) -> None:
        pass

class ConcreteProductA1(ProductA):
    def do_something(self) -> None:
        print("Hello from ConcreteProductA1")

class ConcreteProductA2(ProductA):
    def do_something(self) -> None:
        print("Hello from ConcreteProductA2")

class ProductB(ABC):
    @abstractmethod
    def do_something(self) -> None:
        pass

class ConcreteProductB1(ProductB):
    def do_something(self) -> None:
        print("Hello from ConcreteProductB1")

class ConcreteProductB2(ProductB):
    def do_something(self) -> None:
        print("Hello from ConcreteProductB2")


class AbstractFactory(ABC):
    @abstractmethod
    def create_product_A(self) -> ProductA:
        pass

    @abstractmethod
    def create_product_B(self) -> ProductB:
        pass

class ConcreteFactory1(AbstractFactory):
    def create_product_A(self) -> ProductA:
        return ConcreteProductA1()

    def create_product_B(self) -> ProductB:
        return ConcreteProductB1()

class ConcreteFactory2(AbstractFactory):
    def create_product_A(self) -> ProductA:
        return ConcreteProductA2()

    def create_product_B(self) -> ProductB:
        return ConcreteProductB2()

class FactoryUser:
    def __init__(self, factory: AbstractFactory):
        self.factory: AbstractFactory = factory
        self.initialize()

    def do_something_from_product_A(self) -> None:
        self.productA.do_something()

    def do_something_from_product_B(self) -> None:
        self.productB.do_something()

    def initialize(self) -> None:
        self.productA = self.factory.create_product_A()
        self.productB = self.factory.create_product_B()


if __name__ == "__main__":
    FACTORY_CONFIG_ENV = "2"
    factory: AbstractFactory = None
    if FACTORY_CONFIG_ENV == "1":
        factory = ConcreteFactory1()
    elif FACTORY_CONFIG_ENV == "2":
        factory = ConcreteFactory2()
    factory_user: FactoryUser = FactoryUser(factory=factory)
    factory_user.do_something_from_product_A()
    factory_user.do_something_from_product_B()

