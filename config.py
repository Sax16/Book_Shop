from typing import Dict


class Config:
    SECRET_KEY = '7^d%Y#x^GS&J&9S8'


class DevelopmentConfig(Config):
    DEBUG = True


config: Dict = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
