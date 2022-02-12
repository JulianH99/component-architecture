from abc import ABC, abstractmethod


class Connection(ABC):

    def __init__(self) -> None:
        pass

    @abstractmethod
    def get_driver(self):
        pass

    @abstractmethod
    def open(self) -> None:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
