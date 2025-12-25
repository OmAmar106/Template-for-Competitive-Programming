## here onwards, it is for intersection only, even the point class is different
class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y
def onSegment(p, q, r):
	if ( (q.x <= max(p.x, r.x)) and (q.x >= min(p.x, r.x)) and
		   (q.y <= max(p.y, r.y)) and (q.y >= min(p.y, r.y))):
		return True
	return False
def orientation(p, q, r):
	# to find the orientation of an ordered triplet (p,q,r)
	# function returns the following values:
	# 0 : Collinear points
	# 1 : Clockwise points
	# 2 : Counterclockwise
	val = ((q.y - p.y) * (r.x - q.x)) - ((q.x - p.x) * (r.y - q.y))
	if (val > 0):
		return 1
	elif (val < 0):
		return 2
	else:
		return 0
def doIntersect(p1,q1,p2,q2):
	o1 = orientation(p1, q1, p2)
	o2 = orientation(p1, q1, q2)
	o3 = orientation(p2, q2, p1)
	o4 = orientation(p2, q2, q1)
	if ((o1 != o2) and (o3 != o4)):
		return True
	if ((o1 == 0) and onSegment(p1, p2, q1)):
		return True
	if ((o2 == 0) and onSegment(p1, q2, q1)):
		return True
	if ((o3 == 0) and onSegment(p2, p1, q2)):
		return True
	if ((o4 == 0) and onSegment(p2, q1, q2)):
		return True
	return False
##
## lines
# 2d line: ax + by + c = 0  is  (a, b, c)
#		  ax + by + c = 0	 ((a, b, c),
# 3d line: dx + ez + f = 0  is  (d, e, f),
#		  gy + hz + i = 0	  (g, h, i))

def get_2dline(p1, p2):
	if p1 == p2:
		return (0, 0, 0)
	_p1, _p2 = min(p1, p2), max(p1, p2)
	a, b, c = _p2[1] - _p1[1], _p1[0] - _p2[0], _p1[1] * _p2[0] - _p1[0] * _p2[1]
	g = gcd(gcd(a, b), c)
	return (a // g, b // g, c // g)
dist = lambda p1, p2: sum((a - b) * (a - b) for a, b in zip(p1, p2))**0.5
get_line = lambda p1, p2: map(get_2dline, combinations(p1, 2), combinations(p2, 2))
is_parallel = lambda l1, l2: l1[0] * l2[1] == l2[0] * l1[1]
is_same = lambda l1, l2: is_parallel(l1, l2) and (l1[1] * l2[2] == l2[1] * l1[2])
collinear = lambda p1, p2, p3: is_same(get_2dline(p1, p2), get_2dline(p2, p3))
intersect = (lambda l1, l2: None if is_parallel(l1, l2) else (
	(l2[1] * l1[2] - l1[1] * l2[2]) / (l2[0] * l1[1] - l1[0] * l2[1]),
	(l1[0] * l2[2] - l1[2] * l2[0]) / (l2[0] * l1[1] - l1[0] * l2[1]),
))
rotate = lambda p, theta, origin=(0, 0): (
	origin[0] + (p[0] - origin[0]) * math.cos(theta) - (p[1] - origin[1]) * math.sin(theta),
	origin[1] + (p[0] - origin[0]) * math.sin(theta) + (p[1] - origin[1]) * math.cos(theta),
)
##
## polygons
dist = lambda p1, p2: sum((a - b) * (a - b) for a, b in zip(p1, p2))**0.5
perimeter = lambda *p: sum(dist(i, j) for i, j in zip(p, p[1:] + p[:1]))
area = lambda *p: abs(sum(i[0] * j[1] - j[0] * i[1] for i, j in zip(p, p[1:] + p[:1]))) / 2
is_in_circle = lambda p, c, r: sum(i * i - j * j for i, j in zip(p, c)) < r * r
incircle_radius = lambda a, b, c: area(a, b, c) / (perimeter(a, b, c) / 2)
circumcircle_radius = lambda a, b, c: (dist(a, b) * dist(b, c) * dist(c, a)) / (4 * area(a, b, c))
##