from __future__ import annotations
from abc import ABC, abstractmethod
from config_facade import ConfigFacade


class ConfigHandler(ABC):

    @abstractmethod
    def next_config_handler(self, handler: ConfigHandler) -> ConfigHandler:
        pass

    @abstractmethod
    def create_configuration(self, config):
        pass


class AbstractConfigHandler(ConfigHandler):
    _next_config_handler: ConfigHandler = None

    def next_config_handler(self, handler: ConfigHandler) -> ConfigHandler:
        self._next_config_handler = handler

        return handler

    @abstractmethod
    def create_configuration(self, config):
        if self._next_config_handler:
            return self._next_config_handler.create_configuration(config)

        return None


class FlaskConfigHandler(AbstractConfigHandler):

    def create_configuration(self, config):
        if config['type'] == 'flask':
            return ConfigFacade.get_flask_configuration(config)
        return super().create_configuration(config)


class JsFrameworkConfigHandler(AbstractConfigHandler):
    def create_configuration(self, config):
        if config['type'] == 'js-framework':
            return ConfigFacade.get_jsframework_configuration(config)

        return super().create_configuration(config)


def initialize_chain():
    flask_config_handler = FlaskConfigHandler()

    flask_config_handler.next_config_handler(JsFrameworkConfigHandler())

    return flask_config_handler
