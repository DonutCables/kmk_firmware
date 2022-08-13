print("Starting")

import board
import busio
from digitalio import Pull

from kmk.keys import KC 
from kmk.kmk_keyboard import KMKKeyboard as kb
from kmk.scanners.keypad import KeysScanner
from kmk.modules.encoder_edited import EncoderHandler

from adafruit_mcp230xx.mcp23017 import MCP23017


i2c = busio.I2C(board.D3, board.D2)
mcp = MCP23017(i2c)

enc = EncoderHandler()
kb.modules.append(enc)


def pin(p):
    pin = mcp.get_pin(p)
    pin.pull = Pull.UP
    return pin


enc.pins = ( (board.D0, board.A3, board.A2), (board.D6, board.D5, board.D4), (pin(13), pin(14), pin(15)),
            (board.A0, board.D10, board.A1),(board.D8, board.D7, board.D9), (pin(11), pin(12), pin(10)),
            (pin(6), pin(7), pin(5)), (pin(3), pin(2), pin(4)), (pin(8), pin(9), pin(1)) )
enc.map = [( (KC.A, KC.B, KC.C), (KC.D, KC.E, KC.F), (KC.G, KC.H, KC.I),
            (KC.J, KC.K, KC.L), (KC.M, KC.N, KC.O), (KC.P, KC.Q, KC.R),
            (KC.S, KC.T, KC.U), (KC.V, KC.W, KC.X), (KC.Y, KC.Z, KC.P0) )]


"Block that only exists because you aren't allowed to not have a matrix even with encoderhandler"
kb.matrix = KeysScanner(pins=[board.BUTTON,],)
kb.keymap = [[KC.A,]]


#kb.debug_enabled = True
if __name__ == '__main__':
    kb().go()
