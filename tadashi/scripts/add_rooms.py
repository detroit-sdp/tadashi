import json
n_rooms =int(input("Enter the number of rooms: ")) 

rooms = {}
for room in range(0,n_rooms):
    x = float(input("Enter x coordinate of Room " + str(room+1) + ": "))
    y = float(input("Enter y coordinate of Room " + str(room+1) + ": "))
    r = input("Enter orientation robot should be facing in Room, Options are 'L', 'R', 'F', 'B': ")
    rooms[room+1] = ((x,y),r)

with open('rooms.json', 'w') as f:
    json.dump(rooms, f)
    