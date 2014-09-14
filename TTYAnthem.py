#!/usr/bin/env python

'''
The main interface to TTYAnthem.

Loads the app if it's called directly, otherwise it doesn't do anything.
'''

from TTYAnthem.config import Config
#import argparse


class Loader(object):
    '''
    Loads the app
    '''

    def __init__(self):
        '''
        Initialize the app
        '''
        # Get command line arguments
        #parser = argparse.ArgumentParser()
        #parser.parse_args()

        self.settings = Config()

    def shutdown(self):
        '''
        Shut down the app
        '''

    def daemonize(self):
        '''
        Daemonize app
        '''



if __name__ == "__main__":
    L = None
    try:
        L = Loader()

    except:
        raise
