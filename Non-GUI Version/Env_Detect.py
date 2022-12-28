import os
import sys
import platform


def Get_Host_OS():
    Host_OS = platform.system()
    Architecture = platform.architecture()
    if '64bit' in Architecture:
        bit = '64'
    else:
        bit = '32'
    if Host_OS in {'Windows', 'Linux', 'Darwin'}:      
        Host_OS += bit
    else:
        Host_OS = None
    return Host_OS


def Print_Host_OS():
    OS = Get_Host_OS()
    print(f'Cureent OS: {OS}')