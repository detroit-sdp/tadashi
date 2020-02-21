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