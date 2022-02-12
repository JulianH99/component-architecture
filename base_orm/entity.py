
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, List


class Entity(ABC):

    @abstractmethod
    def find_one(self, **kwargs) -> Entity:
        pass

    @abstractmethod
    def find_all(self, **kwargs) -> List[Entity]:
        pass

    @abstractmethod
    def save(self, **kwargs) -> Entity:
        pass

    @abstractmethod
    def delete(self,  **kwargs) -> Entity:
        pass

    @abstractmethod
    def update(self, id: Any, **kwargs) -> Entity:
        pass
