import os
import yaml
from docker_builder import DockerBuilder, DockerComposeBuilder
from config import MysqlDatabaseConfiguration


class Orchestrator:

    def __init__(self):
        pass

    def set_config_handler(self, config_handler):
        self.config_handler = config_handler

    def set_database_configuration(self, database_configuration):
        self.database_configuration = database_configuration


    def remove_built_packages(self):
        if os.path.isfile(os.path.join(os.getcwd(), 'docker-compose.yml')):
            os.system("docker-compose rm -s -f")

    def collect_packages(self):
        COMPONENT_CONFIG_FILE_NAME = 'config.yml'

        current_dir = os.getcwd()

        components = [f.path for f in os.scandir(
            current_dir) if f.is_dir() and f.name != 'orchestrator' and not f.name.startswith('.')]

        component_configs = {}

        for component_path in components:
            component_name = component_path.split(os.sep)[-1]
            config_file_path = os.path.join(component_path, COMPONENT_CONFIG_FILE_NAME)
            with open(config_file_path, 'r') as config_content:
                loaded_configuration = yaml.safe_load(config_content)
                loaded_configuration['name'] = component_name
                loaded_configuration['path'] = component_path
                component_configs[component_name] = loaded_configuration

        self.components = component_configs

    def configure_packages(self):
        for component in self.components.values():
            configuration = self.config_handler.create_configuration(component)

            DockerBuilder.save_dockerfile(component['path'], configuration)

    def connect_packages(self):
        docker_compose = DockerComposeBuilder()
        mysql_configuration = MysqlDatabaseConfiguration('mysql:5.7') \
            .add_database_user('gardens') \
            .add_database_name('gardens') \
            .add_database_password('gardens') \
            .add_root_password('root')

        docker_compose.add_version() \
            .add_database(mysql_configuration)

        for component in self.components.values():
            docker_compose.add_service(component)

        self.docker_compose_yml = docker_compose.get_configuration(
            lambda config: yaml.dump(config, allow_unicode=True, default_flow_style=False))

    def run_packages(self):
        with open('docker-compose.yml', 'w+') as f:
            f.write(self.docker_compose_yml)
        try:
            os.system("docker-compose up --build")
        except:
            print("Program exited")
