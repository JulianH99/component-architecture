from config_builder import FlaskConfigurationBuilder, JsFrameworkConfigurationBuilder


class ConfigFacade:
    @staticmethod
    def get_flask_configuration(config):
        return FlaskConfigurationBuilder().get_configuration_lines(config)

    @staticmethod
    def get_jsframework_configuration(config):
        return JsFrameworkConfigurationBuilder().get_configuration_lines(config)