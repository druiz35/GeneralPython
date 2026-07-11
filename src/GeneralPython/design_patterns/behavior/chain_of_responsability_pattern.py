from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional

class Handler(ABC):
    @abstractmethod
    def set_next(self, h: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass

class BaseHandler(Handler):
    _next: Handler = None

    def set_next(self, h: Handler) -> Handler:
        self._next = h
        return h

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next:
            return self._next.handle(request)
        return None

class ConcreteHandlerA(BaseHandler):
    def handle(self, request: Any) -> str:
        if request == "A":
            return f"I'm A and I'll process {request}"
        return super().handle(request)

class ConcreteHandlerB(BaseHandler):
    def handle(self, request: Any) -> str:
        if request == "B":
            return f"I'm B and I'll process {request}"
        return super().handle(request)

class ConcreteHandlerC(BaseHandler):
    def handle(self, request: Any) -> str:
        if request == "C":
            return f"I'm C and I'll process {request}"
        return super().handle(request)

def client_code(handler: Handler) -> None:
    for concrete in ["B", "A", "C"]:
        result = handler.handle(concrete)
        if result:
            print(result)
        else:
            print("No result")

if __name__ == "__main__":
    a = ConcreteHandlerA()
    b = ConcreteHandlerB()
    c = ConcreteHandlerC()

    a.set_next(b).set_next(c)
    client_code(a)
    print()
    client_code(b)

