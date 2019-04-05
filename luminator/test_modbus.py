#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division

import pylibmodbus


if __name__ == "__main__":
	mb = pylibmodbus.ModbusTcp("127.0.0.1", 1502)
	mb.connect()
	data = mb.read_registers(0, 1)
	print(list(data))
	mb.close()

