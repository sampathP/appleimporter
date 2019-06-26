# -*- coding: utf-8 -*-


import subprocess


class excmd(object):
    """ Execute the givent command with subprocess"""

    def __init__(self, cmd=None):
        self.pstatus = None
        self.execmd = cmd

    def cmdrun(self, pargs=None):
        """ run the command
        pargs: args to the command
        """

        try:
            self.runcmd = subprocess.Popen(self.execmd,
                                           stdin=subprocess.PIPE,
                                           stdout=subprocess.PIPE,
                                           stderr=subprocess.PIPE)
        except subprocess.CalledProcessError as e:
            print (e.returncode)
            print (e.output)
