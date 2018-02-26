### 2.7x^2 + 3.1x + 2
poly = [2, 3.1, 2.7]

def poly_add2(poly1, poly2):
    new_poly = []
    new_poly.append(poly1[0] + poly2[0])
    new_poly.append(poly1[1] + poly2[1])
    new_poly.append(poly1[2] + poly2[2])
    return new_poly

def poly_mult2(poly1, poly2):
    new_poly = []
    new_poly.append(poly1[0] * poly2[0])
    new_poly.append(poly1[0] * poly2[1] + poly1[1] * poly2[0])
    new_poly.append(poly1[2] * poly2[0] + poly1[1] * poly2[1] + poly1[0] * poly2[2])
    new_poly.append(poly1[2] * poly2[1] + poly1[1] * poly2[2])
    new_poly.append(poly1[2] * poly2[2])
    return new_poly
