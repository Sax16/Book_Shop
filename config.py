from typing import Dict


class Config:
    pass


class DevelopmentConfig(Config):
    DEBUG = True


config :Dict = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
