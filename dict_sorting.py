words = []
with open('words_alpha.txt', 'r') as fin:
    for line in fin:
        words.append(line.replace('\n', ''))
words.sort(key=len)

idx = 1

with open('words_sorted.txt', 'w') as fout:
    for i, word in enumerate(words):
        if len(word) == idx:
            fout.write(str(i + 2) + ', ')
            idx += 1
    fout.write('\n')
    for word in words:
        fout.write(word + '\n')
