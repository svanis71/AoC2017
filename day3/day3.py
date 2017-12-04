import math

class Day3:
    def part1(self):

        target = 289326
        levels = math.ceil(math.sqrt(target))
        last = levels * levels
        diff = last - target

        starty = math.floor(levels / 2)
        startx = math.ceil(levels / 2) - 1

        xdiff = int(math.fabs(diff-startx))
        diff = xdiff + starty
        
        print("levels = %d" % levels)
        print("last = %d, diff = %d" % (last, diff))
        print("start (%d, %d)" % (startx, starty))
        print("xdiff = %d, ydiff = %d, dist = %d" % (xdiff, starty, diff))

        return diff
    
    def part2(self):
        return 0
