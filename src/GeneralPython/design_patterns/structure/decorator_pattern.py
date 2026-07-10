class Component:
    def operation(self) -> str:
        pass

class ConcreteComponent(Component):
    def operation(self) -> str:
        return "ConcreteComponent"

class Decorator(Component):
    _component: Component = None

    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> Component:
        return self._component

    def operation(self) -> str:
        return self._component.operation()

class ConcreteDecoratorA(Decorator):
    def operation(self) -> str:
        return f"ConcreteDecoratorA({self.component.operation()})"

class ConcreteDecoratorB(Decorator):
    def operation(self) -> str:
        return f"ConcreteDecoratorB({self.component.operation()})"

def client_code(component: Component) -> None:
    print(f"RESULT: {component.operation()}\n")

if __name__ == "__main__":
    simple = ConcreteComponent()
    client_code(simple)

    decorator1 = ConcreteDecoratorA(simple)
    client_code(decorator1)
    decorator2 = ConcreteDecoratorB(decorator1)
    client_code(decorator2)
