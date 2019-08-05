#!/bin/python

import sys
import re

print(len(re.findall('[a-zA-Z][^A-Z]*', raw_input().strip())))