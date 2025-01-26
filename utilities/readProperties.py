import configparser

config = configparser.RawConfigParser()
config.read('Configuration/config.ini')

class ReadConfig:

    @staticmethod
    def getBaseURL():
        url=config.get('common info','base_url')
        return url
    @staticmethod
    def getAuthorName():
        author=config.get('test info','author_name')
        return author
