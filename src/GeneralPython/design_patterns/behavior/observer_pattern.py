from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Subscriber(ABC):
    @abstractmethod
    def update(self, context: str):
        pass

class SubscriberA(Subscriber): 
    def get_name(self) -> str:
        return "A"

    def update(self, context: str) -> None:
        if context % 2 == 0:
            print("SubscriberA reacted to event")

class SubscriberB(Subscriber): 
    def get_name(self) -> str:
        return "B"

    def update(self, context: str) -> None:
        if context % 2 != 0:
            print("SubscriberB reacted to event")

class Publisher:
    def __init__(self) -> None:
        self._subscribers = []
        self._main_state = 0

    def subscribe(self, subscriber: Subscriber) -> None:
        self._subscribers.append(subscriber)
        print(f"Publisher: Added new subscriber: {subscriber.get_name()}")

    def unsubscribe(self, subscriber: Subscriber) -> None:
        self._subscribers.remove(subscriber)
        print(f"Publisher: Removed subscriber: {subscriber.get_name()}")

    def notify_subscribers(self) -> None:
        for s in self._subscribers:
            print(f"Publisher: Notifying {self._main_state} to {s.get_name()}")
            s.update(self._main_state)

    def update_main_state(self) -> None:
        self._main_state += 1
        print(f"Publisher: Main state updated to {self._main_state}")
        self.notify_subscribers()

if __name__ == "__main__":
    susA = SubscriberA()
    susB = SubscriberB()
    pub = Publisher()

    pub.update_main_state()
    print()
    pub.subscribe(susA)
    print()
    pub.subscribe(susB)
    print()
    pub.update_main_state()
    print()
    pub.update_main_state()
