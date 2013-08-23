#-*- coding:utf-8 -*-
import os
import yaml

# __all__ = ['configs.CONFIGS','routes.route']

# from configs import CONFIGS
# from routes import Router


class UnparsedContent:
	srcfile = None
	permalink = None

	def __init__(self, srcfile, permalink):
		self.srcfile = srcfile
		self.permalink = permalink

	def parse_conent(self):
		pass
