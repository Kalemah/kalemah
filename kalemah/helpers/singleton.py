#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
    Singleton -- helper class to ease implementing singletons.

    This class sould be inherited from to provide its functionality.
    A Generic Exception is raised when attmting to Inistaceate another Inistace.

    NOTE: 
     Singletons must be inherited once ether directly or through a single subclass of it.

    example:

        >> class Demo(Singleton, ...):
        >>     ...
        >>     ...
        >>     ...
        >>
        >> Demo.hasInstance()
        False
        >> D1 = Demo(..)
        >> Demo.hasInstance()
        True
        >> D2 = Demo(..)
        Traceback (most recent call last):
          File "singleton.py", line 88, in <module>
            D2 = Demo()
          File "singleton.py", line 36, in __init__
            raise Exception(self.exceptionMsg())
        Exception: An Instance of Class 'Demo' Already Exist.
                   Only One Instance Allowed
'''

class Singleton:
    __instance = False

    def __init__(self):
        if self.hasInstance():
            raise Exception(self.exceptionMsg())
        else:
            self.setHasInstance(self)

    @classmethod
    def exceptionMsg(cls):
        classname = str(cls).split('.')[-1]
        return "An Instance of Class '{classname}' Already Exist.\n\t   Only One Instance Allowed".format(classname=classname)

    @classmethod
    def hasInstance(cls):
        return cls.__instance

    @classmethod
    def setHasInstance(cls, obj):
        if not cls.hasInstance() \
        and isinstance(obj,cls):
            cls.__instance=True



