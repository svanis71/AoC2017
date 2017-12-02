#!/usr/bin/env python3

from day1.day1 import Day1
from day2.day2 import Day2

if __name__ == '__main__':
    day1 = Day1()
    print("Day1 pt 1: ")
    print("==============")
    print("Answer is: %d" % day1.part1())
    print("Day1 pt 2: ")
    print("==============")
    print("Answer is: %d" % day1.part2())

    day2 = Day2()
    print("Day2 pt 1: ")
    print("==============")
    print("Answer is: %d" % day2.part1())
    print("Day2 pt 2: ")
    print("==============")
    print("Answer is: %d" % day2.part2())
