class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distanceFromOrigin(self):
        dist = (self.x ** 2 + self.y **2) ** 0.5
        return dist

if __name__ == "__main__":    
    p1 = Point(x=3, y=4)
    print(p1)
    print("Point1 x:", p1.x)
    print("Point1 y:", p1.y)

    print("P1 dist. from origin:", p1.distanceFromOrigin())

    print()
    p2 = Point(8, 15)
    print(p2)
    print("P2 dist. from origin:", p2.distanceFromOrigin())

# class Point():
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def distanceFromOrigin(self):
#         dist = (self.x ** 2 + self.y **2) ** 0.5
#         return dist

# if __name__ == "__main__":
#     point = Point(3, 4)
#     print(point)
#     print(point.x)
#     print(point.distanceFromOrigin())