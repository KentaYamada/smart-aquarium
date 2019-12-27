import os
import logging


# Constants
DEBUG_LOG_KEY = 'debug_logger'
ERROR_LOG_KEY = 'error_logger'
SQL_LOG_KEY = 'sql_logger'


class BaseConfig:
    # Flask config
    DEBUG = False
    ENV = ''
    JSON_AS_ASCII = False
    JSON_SORT_KEYS = True
    TESTING = False
    SECRET_KEY = ''  # required

    # database config
    DATABASE = 'smart_aquarium.db'

    def __str__(self):
        return 'app.config.{0}'.format(type(self).__name__)

    def get_loggin_config(self):
        raise NotImplementedError()

    def get_database_path(self):
        root_path = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(root_path, self.DATABASE)


class ProductionConfig(BaseConfig):
    ENV = 'production'


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    ENV = 'default'
    TESTING = True
    SECRET_KEY = 'secret'

    def get_loggin_config(self):
        log_dir = '{0}/log'.format(os.path.dirname(os.path.abspath(__file__)))
        options = {
            'version': 1,
            'formatters': {
                'devFormat': {
                    'format': '[%(levelname)s] %(asctime)s %(message)s',
                    'datefmt': '%Y-%m-%d %H:%M:%S'
                }
            },
            'handlers': {
                'debug_log_file_handler': {
                    'level': logging.DEBUG,
                    'class': 'logging.FileHandler',
                    'formatter': 'devFormat',
                    'filename': '{0}/debug.log'.format(log_dir),
                },
                'debug_console_handler': {
                    'level': logging.DEBUG,
                    'class': 'logging.StreamHandler',
                    'formatter': 'devFormat'
                },
                'sql_log_file_handler': {
                    'level': logging.DEBUG,
                    'class': 'logging.FileHandler',
                    'formatter': 'devFormat',
                    'filename': '{0}/sql.log'.format(log_dir),
                },
                'error_log_file_handler': {
                    'level': logging.ERROR,
                    'class': 'logging.FileHandler',
                    'formatter': 'devFormat',
                    'filename': '{0}/error.log'.format(log_dir),
                }
            },
            'loggers': {
                DEBUG_LOG_KEY: {
                    'level': logging.DEBUG,
                    'handlers': [
                        'debug_log_file_handler',
                        'debug_console_handler',
                    ],
                    'propagate': 0
                },
                SQL_LOG_KEY: {
                    'level': logging.DEBUG,
                    'handlers': [
                        'sql_log_file_handler'
                    ],
                    'propagate': 0
                },
                ERROR_LOG_KEY: {
                    'level': logging.ERROR,
                    'handlers': [
                        'error_log_file_handler'
                    ],
                    'propagate': 0
                }
            }
        }
        return options


def get_config_by_env():
    """
        Get app configs by env
    """
    configs = {
        'default': DevelopmentConfig(),
        'production': ProductionConfig()
    }
    app_env = os.environ.get('APP_TYPE')
    if app_env not in configs:
        return configs['default']
    return configs[app_env]
