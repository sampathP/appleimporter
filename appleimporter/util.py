# -*- coding: utf-8 -*-
import os
import subprocess
import sys
import traceback


class excmd(object):
    """ Execute the givent command with subprocess"""

    def __init__(self, cmd=None):
        self.pstatus = None
        self.execmd = cmd

    def start(self, pargs=None):
        """ run the command
        pargs: args to the command
        """

        try:
            self.process = subprocess.Popen(self.execmd,
                                            stdin=subprocess.PIPE,
                                            stdout=subprocess.PIPE,
                                            stderr=subprocess.PIPE)
        except subprocess.CalledProcessError as e:
            print (e.returncode)
            print (e.output)

    def run(self, inval=None):
        self.process.stdin.write(b'inval')
        self.process.stdin.flush()
        fo = self.process.stdout.fileno()
        fe = self.process.stderr.fileno()

        def bufread(self, val):
            block_size = 4096
            # Sentinel indicating the end of the output of a sequence of
            # commands.
            # The standard value should be fine.
            rval = b""
            sentinel = b"{ready}"
            while not rval[-32:].strip().endswith(sentinel):
                rval += os.read(val, block_size)
            return rval.strip()[:-len(sentinel)]
        return bufread(fo), bufread(fe)

    def terminate(self):
        self.process.poll()
        if not self.process.returncode():
            self.process.terminate()


class Error(Exception):
    pass


class ProcessExeError(Error):
    # Raised custom error class
    def __init__(self, message):
        self. message = message


def call_process(cmd, spargs=None):

    try:
        proc = subprocess.Popen(cmd,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        pout, perror = proc.communicate()

        if perror and 'Error' in perror.decode('utf-8').split()[0]:
            raise(ProcessExeError(perror.decode('utf-8')))
    except ProcessExeError as e:
        emsg = e.message
        print ("processs exception:", emsg)
    except OSError as e:
        emsg = e.strerror
        print ("exception catch:", emsg)
    except subprocess.CalledProcessError as e:
        emsg = e.message
        print ("exception catch:", emsg)
    except Exception as e:
        t, v, tb = sys.exc_info()
        emsg = traceback.format_exception(t, v, tb)
        print ("exception catch:", emsg)
    else:
        return pout.decode('utf-8')
