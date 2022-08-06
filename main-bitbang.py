print("Starting")

import board
import busio
from digitalio import Direction

from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard as kb
from kmk.handlers.sequences import send_string
from kmk.matrix import DiodeOrientation
from kmk.modules.midi import MidiKeys

from adafruit_mcp230xx.mcp23017 import MCP23017  # type:ignore


# keyboard.debug_enabled = True
kb.modules.append(MidiKeys())
i2c = busio.I2C(board.GP1, board.GP0)
mcp = MCP23017(i2c)


def bpins(p):
    bpin = getattr(board, 'GP{0}'.format(p))
    return bpin


def diopin(p):
    pin = mcp.get_pin(p)
    pin.direction = Direction.OUTPUT
    return pin


#stringslist = [send_string('row{0}col{1}'.format(r, c)) for r in range(16) for c in range(16)]
#alist = [KC.A] * 256
midilist = [KC.MIDI_PC(8, channel=3)]


kb.col_pins = tuple([diopin(p) for p in range(16)],)
kb.row_pins = tuple([bpins(p) for p in range(2, 18)],)
kb.diode_orientation = DiodeOrientation.COLUMNS
kb.keymap = [midilist]


if __name__ == '__main__':
    kb().go()
