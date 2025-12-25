class State:
	def __init__(self):
		self.next = {}
		self.link = -1
		self.len = 0
		self.first_pos = -1
		self.occurrence = 0

class SuffixAutomaton:
	def __init__(self, s):
		self.s = s
		self.states = [State()]
		self.size = 1
		self.last = 0
		for ch in s:
			self.add(ch)
		self._prepare_occurrences() # comment out if taking time
		self._count_substrings()
	def add(self, ch):
		p = self.last
		cur = self.size
		self.states.append(State())
		self.size += 1
		self.states[cur].len = self.states[p].len + 1
		self.states[cur].first_pos = self.states[cur].len - 1
		self.states[cur].occurrence = 1
		while p != -1 and ch not in self.states[p].next:
			self.states[p].next[ch] = cur
			p = self.states[p].link
		if p == -1:
			self.states[cur].link = 0
		else:
			q = self.states[p].next[ch]
			if self.states[p].len + 1 == self.states[q].len:
				self.states[cur].link = q
			else:
				clone = self.size
				self.states.append(State())
				self.size += 1
				self.states[clone].len = self.states[p].len + 1
				self.states[clone].next = self.states[q].next.copy()
				self.states[clone].link = self.states[q].link
				self.states[clone].first_pos = self.states[q].first_pos
				while p != -1 and self.states[p].next[ch] == q:
					self.states[p].next[ch] = clone
					p = self.states[p].link
				self.states[q].link = self.states[cur].link = clone
		self.last = cur
	def _prepare_occurrences(self):
		order = sorted(range(self.size), key=lambda x: -self.states[x].len)
		for i in order:
			if self.states[i].link != -1:
				self.states[self.states[i].link].occurrence += self.states[i].occurrence
	def _count_substrings(self):
		self.dp = [0] * self.size
		for i in range(self.size):
			self.dp[i] = 1
		order = sorted(range(self.size), key=lambda x: self.states[x].len)
		for u in reversed(order):
			for v in self.states[u].next.values():
				self.dp[u] += self.dp[v]
	def is_substring(self, s):
		current = 0
		for ch in s:
			if ch not in self.states[current].next:
				return False
			current = self.states[current].next[ch]
		return True
	def count_occurrences(self, s):
		current = 0
		for ch in s:
			if ch not in self.states[current].next:
				return 0
			current = self.states[current].next[ch]
		return self.states[current].occurrence
	def count_distinct_substrings(self):
		return sum(self.states[i].len - self.states[self.states[i].link].len for i in range(1, self.size))
	def kth_lex_substring(self, k):
		# kth distinct substring
		result = []
		current = 0
		while k:
			for ch in sorted(self.states[current].next):
				next_state = self.states[current].next[ch]
				if self.dp[next_state] < k:
					k -= self.dp[next_state]
				else:
					result.append(ch)
					k -= 1
					current = next_state
					break
		return ''.join(result)
	def enumerate_all_substrings(self):
		result = []
		def dfs(state, path):
			for ch in sorted(self.states[state].next):
				next_state = self.states[state].next[ch]
				result.append(path + ch)
				dfs(next_state, path + ch)
		dfs(0, "")
		return result
	def longest_common_substring(self, t):
		v = 0;l = 0;best = 0;bestpos = 0
		for i in range(len(t)):
			while v and t[i] not in self.states[v].next:
				v = self.states[v].link
				l = self.states[v].len
			if t[i] in self.states[v].next:
				v = self.states[v].next[t[i]]
				l += 1
			if l > best:
				best = l
				bestpos = i
		return t[bestpos - best + 1:bestpos + 1]
	def all_occurrences(self, s):
		current = 0
		for ch in s:
			if ch not in self.states[current].next:
				return []
			current = self.states[current].next[ch]
		positions = []
		def collect(state):
			if self.states[state].occurrence:
				pos = self.states[state].first_pos - len(s) + 1
				positions.append(pos)
			for v in self.states[state].next.values():
				collect(v)
		collect(current)
		return sorted(set(positions))
	def missing_sub(self):
		visited = set()
		q = deque([(0, "")])
		while q:
			state, path = q.popleft()
			for c in map(chr, range(97, 123)):
				if c not in self.states[state].next:
					return path + c
				next_state = self.states[state].next[c]
				if (next_state, path + c) not in visited:
					visited.add((next_state, path + c))
					q.append((next_state, path + c))
		return None