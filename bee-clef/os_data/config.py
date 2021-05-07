import configparser
import os


def getConfig(section, key):
    config = configparser.ConfigParser()
    path = os.path.split(os.path.realpath(__file__))[0] + '/config.conf'
    config.read(path)
    return config.get(section, key)


def setConfig(section, key, value):
    config = configparser.ConfigParser()
    path = os.path.split(os.path.realpath(__file__))[0] + '/config.conf'
    config.read(path)
    config.set("node", "push.url", value)
    return config.get(section, key)



