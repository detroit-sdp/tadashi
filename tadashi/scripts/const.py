#!/usr/bin/env python

ROOMS = {
	1: ((1.98,0.42), 'L'),
	2: ((2,1.75), 'R'),
	'BASE': ((0.0, 0.0), 'F')
}
COMMANDS = {'GOTO', 'LIFT'}

STATUS = {
	-2: 'LOW_BATTERY',
	-1: 'ASSISTANCE',
	 0: 'BASE',
	 1: 'MOVING',
	 2: 'ARRIVED'
}