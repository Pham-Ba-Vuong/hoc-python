import math

class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    
    def __sub__(self, no):
        return Points(
            self.x - no.x,
            self.y - no.y,
            self.z - no.z
        )

    
    def dot(self, no):
        return self.x * no.x + self.y * no.y + self.z * no.z

    
    def cross(self, no):
        return Points(
            self.y * no.z - self.z * no.y,
            self.z * no.x - self.x * no.z,
            self.x * no.y - self.y * no.x
        )
        
    
    def absolute(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(Points(*a))

    a, b, c, d = points[0], points[1], points[2], points[3]


    ab = b - a
    bc = c - b
    cd = d - c

    
    x = ab.cross(bc)
    y = bc.cross(cd)

    cos_phi = x.dot(y) / (x.absolute() * y.absolute())

    angle = math.degrees(math.acos(cos_phi))
    print("%.2f" % angle)
