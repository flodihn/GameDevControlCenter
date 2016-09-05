#!/usr/bin/python
import subprocess
import os

import gdcc_conf

PDFLATEX_CMD = ["pdflatex", os.path.basename(gdcc_conf.GDD_FILE)]

print("Updating Game Documentation Matrix..." + gdcc_conf.GDD_DIR)

subprocess.call(PDFLATEX_CMD, cwd=gdcc_conf.GDD_DIR)
subprocess.call(PDFLATEX_CMD, cwd=gdcc_conf.GDD_DIR)
subprocess.call(["cp", gdcc_conf.GDD_FILE + ".pdf", gdcc_conf.WWW_ROOT])
