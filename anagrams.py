def are_anagrams(str1, str2):
	"""Given 2 strings return true if they are anagrams."""
	
	# Removes spaces to work with anagrams as phrases without punctuation.
	str1 = str1.replace(" ", "")
	str2 = str2.replace(" ", "")

	def count_letters(string):
		"""Creates dictionary that breaks down string into letters and counts."""
		counts = {}
		for letter in string:
			if letter not in counts:
				counts[letter] = 1
			else:
				counts[letter] += 1
		return counts

	counts1 = count_letters(str1)
	counts2 = count_letters(str2)

	if counts1 == counts2:
		return True
	else:
		return False
