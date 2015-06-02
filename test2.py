#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2015 vagrant 
#
# Distributed under terms of the MIT license.

from insert import *
from datetime import datetime, timedelta
today = datetime.now()
start = datetime(2015,5,10)

curr = start
while True:
    try:
        print curr
        download(curr)
    except Exception as e:
        import pdb;pdb.set_trace()
    curr += timedelta(1)
    if curr >= today:
        break


