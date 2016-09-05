#!/usr/bin/python

import subprocess

PATH = "/home/farmgame/FarmingGameDocs/GDD/"
WWW_ROOT = "/var/www/"
PDFLATEX_CMD = ["pdflatex", "GDD"]

print("Updating Game Documentation Matrix..." + PATH)


subprocess.call(PDFLATEX_CMD, cwd=PATH)
subprocess.call(PDFLATEX_CMD, cwd=PATH)
subprocess.call(["cp", PATH + "GDD.pdf", WWW_ROOT])
