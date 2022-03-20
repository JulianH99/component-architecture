from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict


class Config:
    def __init__(self):
        pass


class DatabaseConfiguration(ABC):
    _database_name = ''
    _database_user = ''
    _database_password = ''
    _database_root_password = ''

    _image_name = ''

    def __init__(self, image_name):
        self._image_name = image_name

    def get_image_name(self):
        return self._image_name

    def add_database_name(self, database_name) -> DatabaseConfiguration:
        self._database_name = database_name
        return self

    def add_database_user(self, database_user) -> DatabaseConfiguration:
        self._database_user = database_user
        return self

    def add_database_password(self, database_password) -> DatabaseConfiguration:
        self._database_password = database_password
        return self

    def add_root_password(self, database_root_password) -> DatabaseConfiguration:
        self._database_root_password = database_root_password
        return self

    @abstractmethod
    def environment_config(self) -> Dict:
        pass

    @abstractmethod
    def port_config(self) -> int:
        pass

    def volume_config(self) -> str:
        pass



class MysqlDatabaseConfiguration(DatabaseConfiguration):

    def environment_config(self):
        return {
            'MYSQL_DATABASE': self._database_name,
            'MYSQL_USER': self._database_user,
            'MYSQL_PASSWORD': self._database_password,
            'MYSQL_ROOT_PASSWORD': self._database_root_password
        }

    def port_config(self):
        return 3306

    def volume_config(self):
        return '/var/lib/mysql'