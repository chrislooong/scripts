#!/usr/bin/env python

import autokey
import subprocess

while True:
    url = r"http://www.hdsports.ca/live/nhl/OTT-FLA-20170131/home"
    subprocess.call(['cygstart', url])
    subprocess.call(['sleep', '250'])
    subprocess.call(['cygstart', url])
    subprocess.call(['sleep', '5'])
