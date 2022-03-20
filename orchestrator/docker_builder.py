from __future__ import annotations
from typing import List, Dict, Any, Callable
from pathlib import Path
from config import DatabaseConfiguration
import os


class DockerBuilder:

    @staticmethod
    def save_dockerfile(path: str, lines: List[str]):
        file_path = os.path.join(path, 'Dockerfile')
        file = Path(file_path)
        file.touch(exist_ok=True)
        with open(file, 'w+') as f:
            lines = '\n'.join(lines)
            f.write(lines)


class DockerComposeBuilder:
    DEFAULT_VERSION = '3.5'

    _compose_configuration = {
        'services': {}
    }

    def _format_port(self, local_port: int, remote_port: int):
        return "%s:%s" % (str(local_port), str(remote_port))

    def add_service(self, component: Dict[str, Any]) -> DockerComposeBuilder:
        service_config = {
            'build': component['path'].split(os.sep)[-1],
            'container_name': component['name']
        }

        if 'port' in component:
            service_config['ports'] = [
                self._format_port(component['port'], component['port'])
            ]
        #

        if component['package'] == 'backend' and 'db' in self._compose_configuration['services']:
            service_config['depends_on'] = ['db']
            service_config['environment'] = {'DATABASE_PORT': self.database_configuration.port_config()}

        if 'dependencies' in component:
            if 'depends_on' in service_config:
                service_config['depends_on'].append(component['dependencies'])
            else:
                service_config['depends_on'] = component['dependencies']

        if 'networks' in self._compose_configuration:
            service_config['networks'] = list(self._compose_configuration['networks'].keys())

        self._compose_configuration['services'][component['name']] = service_config

        return self

    def add_network(self) -> DockerComposeBuilder:
        self._compose_configuration['networks'] = {
            'garden-network': {
                'driver': 'bridge'
            }
        }

        return self

    def add_database(self, database_configuration: DatabaseConfiguration) -> DockerComposeBuilder:
        self.database_configuration = database_configuration
        self._compose_configuration['services']['db'] = {
            'image': database_configuration.get_image_name(),
            'container_name': 'database',
            'restart': 'always',
            'ports': [
                self._format_port(database_configuration.port_config(), database_configuration.port_config())
            ],
            'volumes': [
                f'./.database-data/db:{database_configuration.volume_config()}'
            ],
            'environment': database_configuration.environment_config()
        }

        if 'networks' in self._compose_configuration:
            self._compose_configuration['services']['db']['networks'] = list(self._compose_configuration['networks'].keys())

        return self

    def add_version(self) -> DockerComposeBuilder:
        self._compose_configuration['version'] = self.DEFAULT_VERSION
        return self

    def get_configuration(self, transform_function: Callable[[Dict], Any] = None):
        if transform_function:
            return transform_function(self._compose_configuration)

        return self._compose_configuration
