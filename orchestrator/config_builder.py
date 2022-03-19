from typing import List, Dict, Any
from abc import ABC, abstractmethod


class AbstractConfigBuilder(ABC):

    @abstractmethod
    def get_configuration_lines(self, config: Dict[str, Any]):
        pass


class FlaskConfigurationBuilder(AbstractConfigBuilder):

    @staticmethod
    def _get_image() -> str:
        return 'python:3.10-buster'

    @staticmethod
    def _get_workdir(config_name) -> str:
        return f'/app-{config_name}'

    @staticmethod
    def _get_port(port) -> str:
        return f'FLASK_PORT={port}'

    def get_configuration_lines(self, config) -> List[str]:
        config_lines = []

        config_lines.append(f"FROM {self._get_image()}")
        config_lines.append(f"WORKDIR {self._get_workdir(config['name'])}")
        config_lines.extend([
            'RUN apt install libmariadb-dev wget',
            'RUN wget https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh',
            'RUN chmod 777 ./wait-for-it.sh',
            'COPY requirements.txt requirements.txt',
            'RUN pip3 install -r requirements.txt',
            'COPY . .'
        ])

        config_lines.append(f"ENV {self._get_port(config['port'])}")
        config_lines.append(f"EXPOSE {config['port']}")
        config_lines.append("CMD ./wait-for-it.sh -t 60 db:$DATABASE_PORT -- python -m flask run --host=0.0.0.0")

        return config_lines


class JsFrameworkConfigurationBuilder(AbstractConfigBuilder):
    @staticmethod
    def _get_image() -> str:
        return 'node:lts-alpine'

    @staticmethod
    def _get_workdir(config_name: str) -> str:
        return f"/app-{config_name}"

    def get_configuration_lines(self, config) -> List[str]:
        config_lines = []

        config_lines.append(f"FROM {self._get_image()}")
        config_lines.append("RUN npm install -g http-server")
        config_lines.append(f"WORKDIR {self._get_workdir(config['name'])}")
        config_lines.append("COPY package*.json .")
        config_lines.append("RUN npm install")
        config_lines.append("COPY . .")
        config_lines.append(f"RUN {config['build']}")
        config_lines.append(f"ENV PORT={config['port']}")
        config_lines.append(f"EXPOSE {config['port']}")
        config_lines.append(f"CMD [\"http-server\", \"{config['webroot']}\"]")

        return config_lines
