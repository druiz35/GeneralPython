from abc import ABC, abstractmethod
import json

class NewServiceInterface(ABC):
    @abstractmethod
    def do_something(self) -> None:
        pass

class OldService:
    def do_something_old(self) -> None:
        print("Legacy method")

class NewService(NewServiceInterface):
    def do_something(self) -> None:
        print("New method")

class Adapter(NewServiceInterface):
    def __init__(self, legacy_service: OldService):
        self._legacy_service = legacy_service

    def do_something(self):
        self._legacy_service.do_something_old()

class Client:
    def do_something_with_service(self, service: NewServiceInterface):
        service.do_something()


if __name__ == "__main__":
    legacy_service = OldService()
    new_service = NewService()
    adapter = Adapter(legacy_service)
    client = Client()
    client.do_something_with_service(adapter)
    client.do_something_with_service(new_service)
