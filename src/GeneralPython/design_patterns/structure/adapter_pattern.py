class NewService:
    def request(self) -> str:
        return "Target: The default targets' behavior."

class ExistingService:
    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"

class Adapter(NewService, ExistingService):
    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.specific_request()[::-1]}"

class NewNewService:
    def other_specific_request(self) -> str:
        return "Coso coso coso coso"

class NewAdapter(NewNewService, ExistingService):
    def request(self) -> str:
        return f"New Adapter: {self.other_specific_request()}"

if __name__ == "__main__":
    target = NewService()
    print(target.request())
    print("\n")

    adaptee = ExistingService()
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

    adapter = Adapter()
    print(adapter.request(), end="\n\n")

    new_adapter = NewAdapter()
    print(new_adapter.request())
