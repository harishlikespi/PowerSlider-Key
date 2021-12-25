import ctypes
import time, threading
DELAY = 4
def pwsl():
    ctypes.windll.powrprof.PowerSetActiveOverlayScheme(bytes.fromhex("77c71c9647259d4f81747d86181b8a7a")) 
    ctypes.windll.powrprof.PowerSetActiveOverlayScheme(bytes.fromhex("b574d5dea045424f873746345c09c238"))
    threading.Timer(DELAY, pwsl).start()
pwsl()
