# Author: Delainee Lenss
# GitHub username: delainee64
# Date: 11/19/2022
# Description: Write a class named Point that has two data members, x_coord and y_coord,
# representing the two coordinates of the point. Write a class named LineSegment that has two
# data members, endpoint_1 and endpoint_2, representing the two endpoints of the line segment.

class Point:
    """Represents two point data members"""

    def __init__(self, x_coord, y_coord):
        self.__x_coord = x_coord
        self.__y_coord = y_coord

    def get_x_coord(self):
        """Returns the x-coordinate"""
        return self.__x_coord

    def get_y_coord(self):
        """Returns the y-coordinate"""
        return self.__y_coord

    def distance_to(self, other):
        """Returns the distance between both points using the distance formula"""
        return ((self.__x_coord - other.get_x_coord()) ** 2 + (self.__y_coord - other.get_y_coord()) ** 2) ** 0.5


class LineSegment:
    """Represents two endpoints of a line segment"""

    def __init__(self, point1, point2):
        self.__endpoint_1 = point1
        self.__endpoint_2 = point2

    def length(self):
        """Returns the distance between two endpoints"""
        return self.__endpoint_1.distance_to(self.__endpoint_2)

    def get_endpoint_1(self):
        """Returns the first endpoint in a line segment"""
        return self.__endpoint_1

    def get_endpoint_2(self):
        """Returns the second endpoint in a line segment"""
        return self.__endpoint_2

    def is_parallel_to(self, other):
        """Returns whether the line segment is parallel to or not parallel to the line segment being passed"""
        if self.slope() == other.slope():
            return True
        else:
            return False

    def slope(self):
        """Returns the slope of the LineSegment"""
        return (self.__endpoint_2.get_x_coord() - self.__endpoint_1.get_x_coord()) / \
               (self.__endpoint_2.get_y_coord() -
                self.__endpoint_1.get_y_coord())


# point_1 = Point(7, 4)
# point_2 = Point(-6, 18)
# print(point_1.distance_to(point_2))  # prints the distance between points 1 and 2
# line_seg_1 = LineSegment(point_1, point_2)  # a line segment with two points
# print(line_seg_1.length())  # prints the length of the line segment
# print(line_seg_1.slope())  # prints the slope

# point_3 = Point(-2, 2)
# point_4 = Point(24, 12)
# line_seg_2 = LineSegment(point_3, point_4)  # a new line segment with two points
# print(line_seg_1.is_parallel_to(line_seg_2))  # prints if the two line segments are parallel to each other
