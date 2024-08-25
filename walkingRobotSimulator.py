# 874. Walking Robot Simulation
import math

class Solution:
    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        position = [0,0]
        direction = [0,1]
        north = [0,1]
        south = [0,-1]
        east = [1,0]
        west = [-1,0]
        
        maxDistance = 0

        for c in commands:
            if c == -2:
                if direction == north:
                    direction = west
                elif direction == south:
                    direction = east
                elif direction == east:
                    direction = north
                elif direction == west:
                    direction = south
                else:
                    print ('No matches')
                print (direction)
            elif c == -1:
                if direction == north:
                    direction = east
                elif direction == south:
                    direction = west
                elif direction == east:
                    direction = south
                elif direction == west:
                    direction = north
                else:
                    print ('No matches')
                print (direction)
            else:
                for x in range (1,c+1):
                    print (f'The current position is: {position} and direction: {direction}')
                    newPosition = [position[0]+direction[0],position[1]+direction[1]]
                    print (f'New possible: {newPosition}')
                    crash = False
                    for obstacle in  obstacles:
                        if obstacle == newPosition:
                            crash = True
                            break
                    if crash:
                        print ('Possible crash detected')
                        break
                    else:
                        position = newPosition
                        euclidianDistance = position[0]**2 + position[1]**2
                        if euclidianDistance > maxDistance:
                            maxDistance = euclidianDistance
        return maxDistance

        
        