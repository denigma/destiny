# -*- coding: utf-8 -*-


VERSION = (3, 0, 0, "f")
DEV_N = None


def get_version():
    version = "%s.%s" % (VERSION[0], VERSION[1])
    if VERSION[2]:
        version = "%s.%s" % (version, VERSION[2])
    if VERSION[3]:
        version = "%s%s%s" % (version, VERSION[2], VERSION[3])
        if DEV_N:
            version = "%s.dev%s" % (version, DEV_N)
    return version

__version__ = get_version()

__about__ = """
This is the Destiny Denigma, the Digital Decipher Machine.
"""
