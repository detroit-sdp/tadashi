#!/usr/bin/env python
def splitstringbychar(st, c):
	strs = []
	i = 0

	while i < len(st):
		if st[i] != c:
			start = i
			while st[i] != c:
				i+=1
				if i == len(st):
					break
			strs.append(st[start:i])
		else:
			i+=1
		
	return strs

def pointstovector((x1,y1),(x2,y2)):
	return (x2 - x1, y2 - y1)

# st = 'The h ill L s are !!!! alive Wit h Da SuOoUnd of MUSicia..cc         '
# print(splitstringbychar(st, ' '))

# fr = (100.97,9.34)
# to = (10,7)
# print(pointstovector(fr,to))