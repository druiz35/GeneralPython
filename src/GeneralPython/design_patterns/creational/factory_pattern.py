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
        product: Product = create_product()
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
#if __name__ == "__main__":
#    product: Product = None
#    if os.environ["PRODUCT_SETTING"] == "A" or product_setting == "A":
#        product = ConcreteCreatorA.create_product()
#    elif os.environ["PRODUCT_SETTING"] == "B" or product_setting == "B":
#        product = ConcreteCreatorB.create_product()
#    product.do_something()

## A more pythonic implementation
## Instead of a set of class, use a factory standalone method
def build_product(product_setting: str) -> Product:
    if product_setting == "A":
        return ProductA()
    elif product_setting == "B":
        return ProductB()

if __name__ == "__main__":
    product: Product = build_product(product_setting)
    product.do_something()

