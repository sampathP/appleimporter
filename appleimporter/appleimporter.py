# -*- coding: utf-8 -*-

from util import excmd


"""Main module."""


def getfiles(FileName="tetsFile"):
    """ Test Apple Importer method"""
    return FileName


def excute():
    pcmd = excmd('ls -al')
    print pcmd.cmdrun()


if __name__ == "__main__":
    excute()
