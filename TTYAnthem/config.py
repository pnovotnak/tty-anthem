import os
import ConfigParser

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEFAULT_SETTINGS = {
    'GUI': {
        '#': 'GUI configuration section.',

        'type': 'web',
        'listen': '127.0.0.1',
    },

    'TTYs': {
        '#': 'TTYs configuration. Multiple TTYs may be configured here'
    }
}


class Config(object):
    '''
    Config object. When setting a value, persist it to the
    config file defined above.
    '''

    def __init__(self, *args, **kwargs):
        '''
        Set values, provide an interface to override attributes
        '''

        # The default config file
        self.config_file = os.path.join(BASE_DIR, 'config.cfg')

        # Unpack kwargs
        for key in kwargs:

            # Override config file location
            if key == 'config_file':
                self.config_file = kwargs[key]

        self.config = ConfigParser.RawConfigParser(allow_no_value=True)
        self.config.read(self.config_file)

        # Load settings or write defaults
        if self.config.sections():
            pass
        else:
            self.defaults()

    def get(self, section, key):
        '''
        Get a single config value

        Just an alias to ConfigParser.get(section, option)
        '''

        return self.config.get(section, key)

    def set(self, section, key, value):
        '''
        Set a single config value
        '''

        #
        self.config.set(section, key, value)

        # Write out the default settings
        with open(self.config_file, 'wb') as configfile:
            self.config.write(configfile)

        # Reload settings file
        self.config.read(self.config_file)

    def defaults(self):
        '''
        Create a config file if it does not exist and
        set default values
        '''

        config = ConfigParser.RawConfigParser(allow_no_value=True)

        # Parse DEFAULT_SETTINGS dict
        for section in DEFAULT_SETTINGS.keys():
            config.add_section(section)
            for setting in DEFAULT_SETTINGS[section]:
                # Comment lines
                if setting == '#':
                    config.set(section, ' '.join([
                        setting,
                        DEFAULT_SETTINGS[section][setting]
                    ]))
                else:
                    config.set(section, setting, DEFAULT_SETTINGS[section][setting])

        # Write out the default settings
        with open(self.config_file, 'wb') as configfile:
            config.write(configfile)

        # Reload settings file
        self.config.read(self.config_file)