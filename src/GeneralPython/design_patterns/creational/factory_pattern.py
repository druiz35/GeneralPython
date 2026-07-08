from abc import ABC, abstractmethod
import os

# Approach 1: Java-like approach
## Product side
class Product(ABC): 
    @abstractmethod
    def do_something(self) -> None:
        pass

class ProductA(Product):
    def do_something(self) -> None:
        print("HELLO FROM PRODUCT A")

class ProductB(Product):
    def do_something(self) -> None:
        print("HELLO FROM PRODUCT B")

## Factory side
class Creator(ABC):
    @abstractmethod
    def create_product(self) -> Product:
        pass

    def other_method(self) -> None:
        product: Product = self.create_product()
        product.do_something()

class ConcreteCreatorA(Creator):
    @classmethod
    def create_product(cls) -> Product:
        return ProductA()

class ConcreteCreatorB(Creator):
    @classmethod
    def create_product(cls) -> Product:
        return ProductB()

## Hypothetical implementation
product_setting = "B"
def build_product(product_setting: str) -> Product:
    if product_setting == "A":
        return ConcreteCreatorA()
    elif product_setting == "B":
        return ConcreteCreatorB()

if __name__ == "__main__":
    product: Creator = build_product(product_setting)
    product.other_method()

