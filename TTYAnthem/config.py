import os
import ConfigParser

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


class Config(object):
    '''
    Config object. When setting a value, persist it to the
    config file defined above.
    '''

    def __init__(self, **kwargs):
        '''
        Set values, provide an interface to override attributes
        '''

        # The default config file
        self.config_file = os.path.join(BASE_DIR, 'config.cfg')

        # Unpack kwargs
        for key in kwargs:
            print "another keyword arg: %s: %s" % (key, kwargs[key])

        config = ConfigParser.RawConfigParser()
        config.read(self.config_file)

    def get(self, key):
        '''
        Get a config value
        '''


    def defaults(self):
        '''
        Create a config file if it does not exist and
        set default values
        '''

