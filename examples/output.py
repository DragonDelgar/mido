import random
import protomidi
from protomidi.msg import *

import time

out = protomidi.Output()

#
# Play random notes with random programs
#
while 1:
    out.send(program_change(number=random.randrange(128)))    

    note = random.randrange(128)

    out.send(note_on(note=note, velocity=100))
    time.sleep(0.1)

    out.send(note_off(note=note, velocity=100))
    time.sleep(0.1)