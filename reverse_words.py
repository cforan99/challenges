def reverse_words(file):
	f = open(file)
	data = f.read()
	lines = data.split("\n")
	split_lines = []

	for line in lines:
		line = line.rstrip()
		words = line.split()
		words.reverse()
		if len(words) > 0:
			split_lines.append(words)

	for word_list in split_lines:
		s = " "
		print s.join(word_list)
		




# file = open(sys.argv[1], 'r')
# sys.stdout.write(reverse_words(file))
# file.close()