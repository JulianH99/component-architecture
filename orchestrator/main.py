from config_chain import initialize_chain
from config import MysqlDatabaseConfiguration
from orchestrator import Orchestrator



mysql_configuration = MysqlDatabaseConfiguration('mysql:5.7')\
    .add_database_user('gardens')\
    .add_database_name('gardens')\
    .add_database_password('gardens')\
    .add_root_password('root')


config_handler = initialize_chain()

orchestrator = Orchestrator()

orchestrator.set_config_handler(config_handler)
orchestrator.set_database_configuration(mysql_configuration)

orchestrator.remove_built_packages()

orchestrator.collect_packages()
orchestrator.configure_packages()
orchestrator.connect_packages()
orchestrator.run_packages()
