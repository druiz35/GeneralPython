from __future__ import annotations
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

class SimpleCommand(Command):
    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self) -> None:
        print(f"SimpleCommand: Executing simple command with {self._payload}")

class ComplexCommand(Command):
    def __init__(self, receiver: Receiver, a: str, b: str) -> None:
        self._receiver = receiver
        self._a = a
        self._b = b

    def execute(self) -> None:
        print(f"ComplexCommand: Executing complex command with a receiver")
        self._receiver.do_something(self._a)
        self._receiver.do_something_else(self._b)

class Receiver:
    def do_something(self, a: str) -> None:
        print(f"Receiver: Working on {a}")

    def do_something_else(self, b: str) -> None:
        print(f"Receiver: Working on {b}")


class Invoker:
    _on_start = None
    _on_finish = None

    def set_on_start(self, command: Command):
        self._on_start = command

    def set_on_finish(self, command: Command):
        self._on_finish = command

    def do_something_important(self) -> None:
        print("Invoker: Something to do before I start?")
        if isinstance(self._on_start, Command):
            self._on_start.execute()

        print("Invoker: ...doing important shee")

        print("Invoker: Something to do after I'm done?")
        if isinstance(self._on_finish, Command):
            self._on_finish.execute()

if __name__ == "__main__":
    invoker = Invoker()
    invoker.set_on_start(SimpleCommand("First Step"))

    receiver = Receiver()
    invoker.set_on_finish(ComplexCommand(
        receiver, "Do step A", "Do step B"
    ))
    invoker.do_something_important()
