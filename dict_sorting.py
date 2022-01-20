words = []
with open('words_alpha.txt', 'r') as fin:
    for line in fin:
        words.append(line.strip())
words.sort(key=len)

idx = 1

with open('words_sorted.txt', 'w') as fout:
    length_line_seps = []

    # Build the first line of the file, which contains line numbers of where
    # to find words of a specific length. 
    for i, word in enumerate(words): 
        if len(word) == idx:
            length_line_seps.append(str(i))
            idx += 1

    fout.write(','.join(length_line_seps))
    fout.write('\n')

    for word in words:
        fout.write(word + '\n')
