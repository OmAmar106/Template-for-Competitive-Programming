dirs8 = [
	(0, 1),	# 0: up
	(1, 1),	# 1: up-right
	(1, 0),	# 2: right
	(1, -1),   # 3: down-right
	(0, -1),   # 4: down
	(-1, -1),  # 5: down-left
	(-1, 0),   # 6: left
	(-1, 1)	# 7: up-left
]

dir_id = {
	(0, 1): 0,
	(1, 1): 1,
	(1, 0): 2,
	(1, -1): 3,
	(0, -1): 4,
	(-1, -1): 5,
	(-1, 0): 6,
	(-1, 1): 7
}

def rotate_clockwise_45(ind):
	return (ind+1)%8

def rotate_anti_clockwise_45(ind):
	return (ind-1)%8

def reverse(ind):
	return (ind+4)%8

# slash mirror '/'
#
# Light reflecting on:
#
#	 /
#
# slash[d] gives new direction after hitting '/'
slash = [2, 1, 0, 7, 6, 5, 4, 3]
# backslash[d] gives new direction after hitting ''
backslash = [6, 5, 4, 3, 2, 1, 0, 7]
# vertical_mirror[d] gives new direction after hitting '|'
vertical_mirror = [4, 3, 2, 1, 0, 7, 6, 5]
horizontal_mirror = [4, 5, 6, 7, 0, 1, 2, 3]

def extras():
	# use Decimal(number) for context to work
	# slows down the code significantly
	# by default, there is precision of 10-6
	getcontext().prec = 50
	# more precision, use Fraction
	from fractions import Fraction
	sys.setrecursionlimit(10**6)
	sys.set_int_max_str_digits(10**5)
# extras()

def interactive():
	import builtins
	# print(globals())
	globals()['print'] = lambda *args, **kwargs: builtins.print(*args, flush=True, **kwargs)
# interactive()

def reduce_time():
	# reduces run time, but increases the chance of mle
	import gc
	gc.disable()
# reduce_time()

ordalp = lambda s : ord(s)-65 if s.isupper() else ord(s)-97
alp = lambda x : chr(97+x)
yes = lambda : print("Yes")
no = lambda : print("No")
yn = lambda flag : print("Yes" if flag else "No")
printf = lambda x : print(-1 if x==float('inf') else x)
lalp = 'abcdefghijklmnopqrstuvwxyz'
ualp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
dirs = ((1,0),(0,1),(-1,0),(0,-1))
dirs8 = ((1,0),(0,1),(-1,0),(0,-1),(1,-1),(-1,1),(1,1),(-1,-1))
ldir = {'D':(1,0),'U':(-1,0),'R':(0,1),'L':(0,-1)}

def GI(n,m=None,sub=-1,dirs=False,weight=False):
	if m==None:
		m = n-1
	d = [[] for i in range(n)]
	if not weight:
		for i in range(m):
			u,v = LII_C(lambda x:int(x)+sub)
			d[u].append(v)
			if not dirs:
				d[v].append(u)
	else:
		for i in range(m):
			u,v,w = LII()
			d[u+sub].append((v+sub,w))
			if not dirs:
				d[v+sub].append((u+sub,w))
	return d
