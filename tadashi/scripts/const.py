#!/usr/bin/env python
import json

with open('rooms.json') as f:
    ROOMS = json.load(f)
for x in ROOMS:
    ROOMS[x][0] = tuple(ROOMS[x][0])
    ROOMS[x] = tuple(ROOMS[x])
ROOMS['BASE'] = ((0.0,0.0),'F')

COMMANDS = {'GOTO', 'LIFT'}

STATUS = {
	-2: 'LOW_BATTERY',
	-1: 'ASSISTANCE',
	 0: 'BASE',
	 1: 'MOVING',
	 2: 'ARRIVED'
}
