#!/usr/bin/python3
"""
this will del
and cash
"""

import os
from fabric.api import *

env.hosts = ['100.26.210.153', '100.26.155.94']


def do_clean(number=0):
    """
    This will del any cash 
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
