import os

class config:
    '''
    general configuration parent class
    '''
    NEWS_API_BASE_URL='https://newsapi.org/v2/sources?&category={}&apiKey={}'
    NEWS_API_KEY=os.environ.get('NEWS_API_KEY')

class ProdConfig(config):
    pass

class DevConfig(config):
    DEBUG=True


config_options={
    'development':DevConfig,
    'production':ProdConfig
}