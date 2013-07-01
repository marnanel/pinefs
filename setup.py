#!/usr/bin/env python

from distutils.core import setup

import vers

setup (name="Pinefs",
       version= vers.version,
       author = "Aaron Lav",
       author_email = "asl2@pobox.com",
       license = "X",
       description = 'Python NFS server and ONC RPC compiler',
       long_description = """Python implementation of NFS v2 server,
       implementing a simple in-memory filesystem, a filesystem view
       of the Python namespace, and a tar filesystem.  Includes rpcgen,
       an IDL compiler.""",
       platforms = "Any Python 2.2 or later",
       url = "http://www.pobox.com/~asl2/software/Pinefs")

