### Point Point -> (int)Distance
def distance(p1, p2):
    return ((p2.x - p1.x)**2 + (p2.y - p1.y)**2)**(1/2)

### Circle Circle -> (boolean)Overlap?
def circles_overlap(c1, c2):
    return distance(c1.point, c2.point) < (c1.radius + c2.radius)
