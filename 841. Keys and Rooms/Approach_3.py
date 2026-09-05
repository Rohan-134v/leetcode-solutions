class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        stack = [0]
        while stack:
            currentRoom = stack.pop()
            visited.add(currentRoom)
            for room in rooms[currentRoom]:
                if room not in visited:
                    stack.append(room)
        return len(visited) == len(rooms)

