class BitSet:
	ADDRESS_BITS_PER_WORD = 12
	BITS_PER_WORD = 1 << ADDRESS_BITS_PER_WORD
	WORD_MASK = -1
	def __init__(self, sz):
		self.sz = sz
		self.words = [0] * (self._wordIndex(sz - 1) + 1)
	def _wordIndex(self, bitIndex):
		if bitIndex >= self.sz:
			raise ValueError("out of bound index", bitIndex)
		return bitIndex >> BitSet.ADDRESS_BITS_PER_WORD
	def flip(self, bitIndex):
		wordIndex = self._wordIndex(bitIndex)
		self.words[wordIndex] ^= 1 << (bitIndex % BitSet.BITS_PER_WORD)
	def flip_range(self, l, r):
		startWordIndex = self._wordIndex(l)
		endWordIndex = self._wordIndex(r)
		firstWordMask = BitSet.WORD_MASK << (l % BitSet.BITS_PER_WORD)
		rem = (r+1) % BitSet.BITS_PER_WORD
		lastWordMask = BitSet.WORD_MASK if rem == 0 else ~(BitSet.WORD_MASK << rem)
		if startWordIndex == endWordIndex:
			self.words[startWordIndex] ^= (firstWordMask & lastWordMask)
		else:
			self.words[startWordIndex] ^= firstWordMask
			for i in range(startWordIndex + 1, endWordIndex):
				self.words[i] ^= BitSet.WORD_MASK
			self.words[endWordIndex] ^= lastWordMask
	def __setitem__(self, bitIndex, value):
		wordIndex = self._wordIndex(bitIndex)
		if value:
			self.words[wordIndex] |= 1 << (bitIndex % BitSet.BITS_PER_WORD)
		else:
			self.words[wordIndex] &= ~(1 << (bitIndex % BitSet.BITS_PER_WORD))
	def __getitem__(self, bitIndex):
		wordIndex = self._wordIndex(bitIndex)
		return self.words[wordIndex] & (1 << (bitIndex % BitSet.BITS_PER_WORD)) != 0
	def nextSetBit(self, fromIndex):
		wordIndex = self._wordIndex(fromIndex)
		word = self.words[wordIndex] & (BitSet.WORD_MASK << (fromIndex % BitSet.BITS_PER_WORD))

		while True:
			if word != 0:
				return wordIndex * BitSet.BITS_PER_WORD + (word & -word).bit_length() - 1
			wordIndex += 1
			if wordIndex > len(self.words) - 1:
				return -1
			word = self.words[wordIndex]
	def nextClearBit(self, fromIndex):
		wordIndex = self._wordIndex(fromIndex)
		word = ~self.words[wordIndex] & (BitSet.WORD_MASK << (fromIndex % BitSet.BITS_PER_WORD))

		while True:
			if word != 0:
				index = wordIndex * BitSet.BITS_PER_WORD + (word & -word).bit_length() - 1
				return index if index < self.sz else - 1
			wordIndex += 1
			if wordIndex > len(self.words) - 1:
				return -1
			word = ~self.words[wordIndex]
	def lastSetBit(self):
		wordIndex = len(self.words) - 1
		word = self.words[wordIndex]

		while wordIndex >= 0:
			if word != 0:
				return wordIndex * BitSet.BITS_PER_WORD + (word.bit_length() - 1 if word > 0 else  BitSet.BITS_PER_WORD - 1)
			wordIndex -= 1
			word = self.words[wordIndex]
		return -1
	def __str__(self):
		res = []
		st = 0
		while True:
			i = self.nextSetBit(st)
			if i != -1:
				res += [0] * (i - st)
				j = self.nextClearBit(i)
				if j != -1:
					res += [1] * (j-i)
					st = j
				else:
					res += [1] * (self.sz - i)
					break
			else:
				res += [0] * (self.sz - st)
				break

		return "".join(str(v) for v in res)
	def __repr__(self):
		return "Bitset(%s)" % str(self)
	def __iter__(self):
		for i in self[:]:
			yield i
	def __len__(self):
		return self.sz
	def __or__(self, other):
		if self.sz != other.sz:
			raise ValueError("BitSets must be of equal size")
		res = BitSet(self.sz)
		res.words = [a | b for a, b in zip(self.words, other.words)]
		return res
	def __add__(self, other):
		if self.sz != other.sz:
			raise ValueError("BitSets must be of equal size")
		res = BitSet(self.sz)
		carry = 0
		for i in range(len(self.words)):
			total = self.words[i] + other.words[i] + carry
			res.words[i] = total & BitSet.WORD_MASK
			carry = total >> BitSet.BITS_PER_WORD
		return res
	def __and__(self, other):
		if self.sz != other.sz:
			raise ValueError("BitSets must be of equal size")
		res = BitSet(self.sz)
		res.words = [a & b for a, b in zip(self.words, other.words)]
		return res
	def __xor__(self, other):
		if self.sz != other.sz:
			raise ValueError("BitSets must be of equal size")
		res = BitSet(self.sz)
		res.words = [a ^ b for a, b in zip(self.words, other.words)]
		return res
	def __invert__(self):
		res = BitSet(self.sz)
		res.words = [~a & BitSet.WORD_MASK for a in self.words]
		return res
	def add(self, val):
		self.flip_range(val, self.nextClearBit(val))
	def rem(self, val):
		self.flip_range(val, self.nextSetBit(val))