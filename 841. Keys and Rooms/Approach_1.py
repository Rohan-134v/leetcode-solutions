class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = {0}
        stack = [0]

        while stack:
            currentRoom = stack.pop()
            for room in rooms[currentRoom]:
                if room not in visited:
                    visited.add(room)
                    stack.append(room)
        
        return len(visited) == len(rooms)

