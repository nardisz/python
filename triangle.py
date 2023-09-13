def equilateral(a, b, c):
    if a != 0 and b != 0 and c != 0:
        if a + b >= c and a + c >= b and b + c >= a:
            if a == b == c:
                return True
    return False

def isosceles(a, b, c):
    if a != 0 and b != 0 and c != 0:
        if a + b >= c and a + c >= b and b + c >= a:
            if a == b or a == c or b == c:
                return True
    return False


def scalene(a, b, c):
    if a != 0 and b != 0 and c != 0:
        if a + b >= c and a + c >= b and b + c >= a:
            if a != b and b != c and a != c:
                return True
    return False