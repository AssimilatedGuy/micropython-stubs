"""
Module: 'parameters_c' on LEGO EV3 v1.0.0
"""
# MCU: sysname=ev3, nodename=ev3, release=('v1.0.0',), version=('0.0.0',), machine=ev3
# Stubber: 1.3.2

class Button:
    def __init__(self, *args):
        ''
        pass

    BEACON = 256
    CENTER = 32
    DOWN = 4
    LEFT = 16
    LEFT_DOWN = 2
    LEFT_UP = 128
    RIGHT = 64
    RIGHT_DOWN = 8
    RIGHT_UP = 512
    UP = 256

class Color:
    def __init__(self, *args):
        ''
        pass

    BLACK = 1
    BLUE = 2
    BROWN = 7
    GREEN = 3
    ORANGE = 8
    PURPLE = 9
    RED = 5
    WHITE = 6
    YELLOW = 4

class Direction:
    def __init__(self, *args):
        ''
        pass

    CLOCKWISE = 0
    COUNTERCLOCKWISE = 1

class Port:
    def __init__(self, *args):
        ''
        pass

    A = 65
    B = 66
    C = 67
    D = 68
    S1 = 49
    S2 = 50
    S3 = 51
    S4 = 52

class Stop:
    def __init__(self, *args):
        ''
        pass

    BRAKE = 1
    COAST = 0
    HOLD = 2
