import os
import yaml
import shutil
from typing import Dict, Any

from config_chain import initialize_chain
from docker_builder import DockerBuilder, DockerComposeBuilder
from config import MysqlDatabaseConfiguration

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

# initialize chain
config_handler = initialize_chain()


def get_component_build_order(components: Dict[str, Any]):
    components_with_dependencies = list(
        filter(lambda cc: 'dependencies' in component_configs[cc], component_configs.keys()))

    component_build_order = []

    for component_with_dependencies in components_with_dependencies:
        dependencies = components[component_with_dependencies]['dependencies']
        for dependency in dependencies:
            if dependency not in component_build_order:
                component_build_order.append(dependency)

    for component in components.keys():
        if component not in component_build_order:
            component_build_order.append(component)

    return component_build_order


component_build_order = get_component_build_order(component_configs)

docker_compose = DockerComposeBuilder()
mysql_configuration = MysqlDatabaseConfiguration('mysql:5.7')\
    .add_database_user('gardens')\
    .add_database_name('gardens')\
    .add_database_password('gardens')\
    .add_root_password('root')

docker_compose.add_version() \
    .add_database(mysql_configuration)

for component in component_build_order:
    configuration = config_handler.create_configuration(component_configs[component])

    DockerBuilder.save_dockerfile(component_configs[component]['path'], configuration)
    docker_compose.add_service(component_configs[component])


#
docker_compose_yml = docker_compose.get_configuration(
    lambda config: yaml.dump(config, allow_unicode=True, default_flow_style=False))


with open('docker-compose.yml', 'w+') as f:
   f.write(docker_compose_yml)

# run docker compose
try:
    os.system("docker-compose up")
except:
    print("Program exited")

