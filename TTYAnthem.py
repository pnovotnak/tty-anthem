#!/usr/bin/env python

import argparse


class Loader(object):

    def __init__(self):

        # Get command line arguments
        parser = argparse.ArgumentParser()
        parser.parse_args()


if __name__ == "__main__":
    l = None
    try:
        l = Loader()
    except:
        raise
