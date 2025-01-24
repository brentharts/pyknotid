#!/usr/bin/env python3
import os, sys, subprocess
import numpy, networkx, sympy, appdirs, requests, tqdm
_thisdir = os.path.split(os.path.abspath(__file__))[0]

try:
	import planarity
except ModuleNotFoundError:
	pass

try:
	import peewee
except ModuleNotFoundError:
	print('peewee not installed')

try:
	import vizpy
except ModuleNotFoundError:
	print('vizpy not installed')

sys.path.append(_thisdir)
import pyknotid
print(pyknotid)
import pyknotid.spacecurves as sp
print(sp)
import pyknotid.make as mk
print(mk)
