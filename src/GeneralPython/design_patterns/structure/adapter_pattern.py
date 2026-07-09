class NewService:
    def request(self) -> str:
        return "Target: The default targets' behavior."

class ExistingService:
    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"

class Adapter(NewService, ExistingService):
    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.specific_request()[::-1]}"

def client_code(target: "NewService") -> None:
    print(target.request(), end="")

if __name__ == "__main__":
    target = NewService()
    client_code(target)
    print("\n")

    adaptee = ExistingService()
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

    adapter = Adapter()
    client_code(adapter)
