#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import zipfile

with zipfile.ZipFile(sys.argv[1], "r") as zipped_file:
    zipped_file.extractall()
