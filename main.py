# -*- coding: utf-8 -*-

__all__ = ()

if __name__ != '__main__':
    raise Exception('main.py is meant to be run directly.')

from os import chdir, path
from utils import ensure_config

from objects.aika import Aika

chdir(path.dirname(path.realpath(__file__)))

if ensure_config():
    aika = Aika()
    aika.run() # blocking call
