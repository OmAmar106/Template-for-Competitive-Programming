def extras():
	getcontext().prec = 50
	sys.setrecursionlimit(10**6)
	sys.set_int_max_str_digits(10**5)
# extras()

def interactive():
	import builtins
	# print(globals())
	globals()['print'] = lambda *args, **kwargs: builtins.print(*args, flush=True, **kwargs)
# interactive()

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