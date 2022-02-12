from abc import ABC, abstractmethod
from typing import Any, List, Union

from base_orm.connection import Connection


class Query(ABC):

    def __init__(self, connection: Connection) -> None:
        self.connection = connection

    @abstractmethod
    def execute(self, query_str: str, params: List[Any]) -> Union[List[Any], Any]:
        pass
