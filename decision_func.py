from dkeys import PressKey,ReleaseKey, W, A, S, D
import time


val=4

def straight(time_):
    PressKey(W)
    time.sleep(time_/val)
    ReleaseKey(W)

def left(time_):
    PressKey(A)
    time.sleep(time_/val)
    ReleaseKey(A)
    
def right(time_):
    PressKey(D)
    time.sleep(time_/val)
    ReleaseKey(D)

def reverse(time_):
    PressKey(S)
    time.sleep(time_/val)
    ReleaseKey(S)
    
def blank(): 
    ReleaseKey(W)
    ReleaseKey(A)
    ReleaseKey(S)
    ReleaseKey(D)