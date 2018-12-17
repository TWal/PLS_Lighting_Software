import readline
import code
import rlcompleter

from dmx import *
from fixtures import *
from color import *
from effects import *

if __name__ == "__main__":
    washs = [Wash(1+29*i) for i in range(8)]
    w = washs[1]
    w.color = Color(1,0,0)
    dmx = DMX(washs, [EffectHue(w)])
    # dmx = DMX(washs, [])
    dmx.start()

    readline.parse_and_bind("tab: complete")
    variables = globals().copy()
    variables.update(locals())
    shell = code.InteractiveConsole(variables)
    shell.interact()

    dmx.stop()
