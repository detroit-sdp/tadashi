#!/usr/bin/env python

ROOMS = {
	1: ((0.0,0.0), 'R'),
	2: ((0.0,0.0), 'L'),
	'BASE': ((0.0,0.0), 'F')
}

COMMANDS = {'GOTO', 'LIFT'}

STATUS = {
	-2: 'LOW_BATTERY',
	-1: 'ASSISTANCE',
	 0: 'BASE',
	 1: 'MOVING',
	 2: 'ARRIVED'
}