# -*- coding: utf-8 -*-
from socket import gaierror

from mpd import MPDClient
from config import MPD_SRV

srv = MPDClient()

def conn(func):
    def wrapper(*args):
        try:
            srv.connect(MPD_SRV['host'], MPD_SRV['port'])
            srv.password(MPD_SRV['passwd'])
            func(*args)
            srv.disconnect()
        except gaierror as e:
            print 'oops: ' + e.__str__()

    return wrapper

@conn
def init():
    srv.repeat(1)

@conn
def dec_vol():
    volume = int(srv.status()['volume'])
    if volume > 50:
        volume -= 2
        srv.setvol(volume)
        print "volume dereased to " + str(volume)
    else:
        print "volume at minimum"

@conn
def inc_vol():
    volume = int(srv.status()['volume'])
    if volume < 99:
        volume += 2
        srv.setvol(volume)
        print "volume inreased to " + str(volume)
    else:
        print "volume at maximum"

@conn
def play(uri):
    srv.clear()
    srv.load(uri)
    srv.play(0)

@conn
def stop():
    srv.stop()
    srv.clear()
