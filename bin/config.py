import sys

if sys.version_info[0] == 2:
    import ConfigParser as configparser
else:
    import configparser

config = configparser.ConfigParser()


class configuration(object):

    def getDbDatabase(self):
        self.readConfig()

        return config.get('DB', 'database')

    def getDbPort(self):
        self.readConfig()

        return config.get('DB', 'port')

    def getDbHost(self):
        self.readConfig()

        return config.get('DB', 'host')

    def getDbPassword(self):
        self.readConfig()

        return config.get('DB', 'password')

    def getDbUser(self):
        self.readConfig()

        return config.get('DB', 'user')

    def readConfig(self):
        property = config.read('config')

        return property
