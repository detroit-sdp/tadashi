#!/usr/bin/env python

ROOMS = {
	1: ((0.797,3.14), 'R'),
	2: ((-6.5,-0.5), 'R'),
	3: ((-6.24,3.52), 'B'),
	4: ((5.6,-1.8), 'R'),
	'BASE': ((-2.53, 4.0), 'F')
}

COMMANDS = {'GOTO', 'LIFT'}

STATUS = {
	-2: 'LOW_BATTERY',
	-1: 'ASSISTANCE',
	 0: 'BASE',
	 1: 'MOVING',
	 2: 'ARRIVED'
}