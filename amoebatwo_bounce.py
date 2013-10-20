#!/usr/bin/env python3

import amoebatwo
import time
import sys

m = amoebatwo.AmoebaTwo()

triggered = False;

def stop(event):
	m.move.stop();
	triggered = True;

m.registerListener(0, stop);
m.registerListener(1, stop);

m.move.forwards();

