
class Trie:
	def __init__(self, *words):
		self.root = {}
		for word in words:
			self.add(word)

	def add(self, word):
		current_dict = self.root
		for letter in word:
			current_dict = current_dict.setdefault(letter, {})
		current_dict[0] = True

	def __contains__(self, word):
		current_dict = self.root
		for letter in word:
			if letter not in current_dict:
				return False
			current_dict = current_dict[letter]
		return 0 in current_dict

	def __delitem__(self, word):
		current_dict = self.root
		nodes = [current_dict]
		for letter in word:
			current_dict = current_dict[letter]
			nodes.append(current_dict)
		del current_dict[0]