from abc import ABC, abstractmethod

# NOTE: Here the products are the same, but in reality they could have different
#       building steps
class Product1:
    def __init__(self):
        self.featureA:str = "default"
        self.featureB:str = "default"
        self.featureZ:str = "default"

    def setFeatureA(self, value: str) -> None:
        self.featureA = value

    def setFeatureB(self, value: str) -> None:
        self.featureB = value

    def setFeatureZ(self, value: str) -> None:
        self.featureZ = value

    def __str__(self):
        return f"A:{self.featureA}/n B:{self.featureB}/n Z:{self.featureZ}"

class Product2:
    def __init__(self):
        self.featureA:str = "default"
        self.featureB:str = "default"
        self.featureZ:str = "default"
    
    def setFeatureA(self, value: str) -> None:
        self.featureA = value

    def setFeatureB(self, value: str) -> None:
        self.featureB = value

    def setFeatureZ(self, value: str) -> None:
        self.featureZ = value

    def __str__(self):
        return f"A:{self.featureA}/n B:{self.featureB}/n Z:{self.featureZ}"


class Builder(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def buildStepA(self):
        pass

    @abstractmethod
    def buildStepB(self):
        pass

    @abstractmethod
    def buildStepZ(self):
        pass

class ConcreteBuilder1(Builder):
    def __init__(self):
        self.result: Product1 = None

    def reset(self) -> None:
        self.result = Product1()

    def buildStepA(self) -> None:
        self.result.setFeatureA("This is feature A for product 1")

    def buildStepB(self) -> None:
        self.result.setFeatureB("This is feature B for product 1")

    def buildStepZ(self) -> None:
        self.result.setFeatureZ("This is feature Z for product 1")

    def getResult(self) -> Product1:
        return self.result

class ConcreteBuilder2(Builder):
    def __init__(self):
        self.result: Product2 = None

    def reset(self) -> None:
        self.result = Product2()

    def buildStepA(self) -> None:
        self.result.setFeatureA("This is feature A for product 2")

    def buildStepB(self) -> None:
        self.result.setFeatureB("This is feature B for product 2")

    def buildStepZ(self) -> None:
        self.result.setFeatureZ("This is feature Z for product 2")

    def getResult(self) -> Product2:
        return self.result

class Director:
    def __init__(self, builder: Builder):
        self.builder = builder

    def change_builder(self, builder: Builder) -> None:
        self.builder = builder

    def make(self, type: str) -> None:
        self.builder.reset()
        if type == "1":
            self.builder.buildStepA()
        elif type == "2":
            self.builder.buildStepB()
            self.builder.buildStepZ()

# "client" side
if __name__ == "__main__":
    BUILDER_ENV = "1"
    if BUILDER_ENV == "1":
        b = ConcreteBuilder1()
    elif BUILDER_ENV == "2":
        b = ConcreteBuilder2()
    d = Director(builder=b)
    d.make(BUILDER_ENV)
    print(b.getResult())
