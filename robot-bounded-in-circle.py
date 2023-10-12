class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direc = [0,1]
        pos = [0,0]
        for t in range(4):
            for char in instructions:
                if char == 'G':
                    pos[0] += direc[0]
                    pos[1] += direc[1]
                elif char == 'L':
                    if direc == [0,1]:
                        direc = [1,0]
                    elif direc == [1,0]:
                        direc = [0,-1]
                    elif direc == [0,-1]:
                        direc = [-1,0]
                    elif direc == [-1,0]:
                        direc = [0,1]
                elif char == 'R':
                    if direc == [0,1]:
                        direc = [-1,0]
                    elif direc == [-1,0]:
                        direc = [0,-1]
                    elif direc == [0,-1]:
                        direc = [1,0]
                    elif direc == [1,0]:
                        direc = [0,1]
        if pos == [0,0]:
            return True