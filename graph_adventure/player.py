class Player:
    def __init__(self, name, startingRoom):
        self.name = name
        self.currentRoom = startingRoom
        self.visited_rooms = {self.currentRoom}

    def travel(self, direction, showRooms = False):
        nextRoom = self.currentRoom.getRoomInDirection(direction)
        if nextRoom is not None:
            self.currentRoom = nextRoom
            self.visited_rooms.add(self.currentRoom)
            if (showRooms):
                nextRoom.printRoomDescription(self)

    
    def get_unvisited_directions(self):
        directions = []

        if ((self.currentRoom.n_to not in self.visited_rooms) and (self.currentRoom.n_to is not None)):
            directions.append('n')
        if ((self.currentRoom.s_to not in self.visited_rooms) and (self.currentRoom.s_to is not None)):
            directions.append('s')
        if ((self.currentRoom.e_to not in self.visited_rooms) and (self.currentRoom.e_to is not None)):
            directions.append('e')
        if ((self.currentRoom.w_to not in self.visited_rooms) and (self.currentRoom.w_to is not None)):
            directions.append('w')
        
        return directions


    def get_unique_rooms_visited(self):
        return len(self.visited_rooms)
        