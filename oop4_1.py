from point import Point
import copy

class LineSegment:
    def __init__(self, *args):
        if len(args) == 0:
            self.__d1 = Point(0, 5)
            self.__d2 = Point(1, 0)
        if len(args) == 2:
            if isinstance(args[0], Point):
                self.__d1 = args[0]
                self.__d2 = args[1]
        if len(args) == 4:
            if isinstance(args[0], int):
                self.__d1 = Point(args[0], args[1])
                self.__d2 = Point(args[2], args[3])
        if len(args) == 1:
            if isinstance(args[0], LineSegment):
                self.__d1 = copy.deepcopy(args[0].__d1)
                self.__d2 = copy.deepcopy(args[0].__d2)

    def __str__(self):
        return "[(%d,%d),(%d,%d)]" % (self.__d1.X(), self.__d1.Y(), self.__d2.X(), self.__d2.Y())

    def getD1(self):
        return self.__d1

    def getD2(self):
        return self.__d2