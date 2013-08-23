#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import yaml

from .helpers.singleton import Singleton

class Configs(Singleton):

    config_path         = os.path.abspath("configs.yml")
    cache_dirctory      = os.path.abspath("cache/")
    content_dirctory    = os.path.abspath("content/")
    markdown_extension  = 'md'

    def __init__(self):
        Singleton.__init__(self)
        self.update()

        self.cache_dirctory   = os.path.abspath( self.cache_dirctory )   + '/'
        self.content_dirctory = os.path.abspath( self.content_dirctory ) + '/'
        
        # self.resetDefualts()

    # def resetDefualts(self):
    #     if not self.cache_dirctory:
    #         self.cache_dirctory = os.path.abspath("cache/")

    #     if not self.content_dirctory:
    #         self.content_dirctory = os.path.abspath("content/")

    def inspect(self):
        inspectstr = yaml.dump(self.__dict__, default_flow_style=False, indent=2)
        return inspectstr.replace('\n','<br>').replace(' ','&nbsp;')

    def update(self):
        ''' Update configs from config file '''
        self.__dict__.update( yaml.load( file(self.config_path, 'r') ) )

    def keys(self):
        ''' list of configs keys'''
        return self.__dict__.keys()

CONFIGS = Configs()
