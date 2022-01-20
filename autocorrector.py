from Levenshtein import distance as lev_dis


class Autocorrector:

    def __init__(self, dict_path: str):
        self.words = {}
        self.largest_word_len = 0

        with open(dict_path, 'r') as fin:
            length_line_seps = [
                int(sep.strip()) for sep in fin.readline().strip().split(",")
            ]

            # Assume that there are no gaps between word lengths
            # (ie. if we have words of length 5 and 7, then we also have 6).
            self.largest_word_len = len(length_line_seps)

            # Add none to simplify popping at end of file.
            length_line_seps.append(None)

            curr_size = 0
            curr_line = 0

            for line in fin:
                # Check what size the string is using the seps,
                # without doing str comparisons.
                if curr_line == length_line_seps[0]:
                    curr_size += 1
                    self.words[curr_size] = []
                    length_line_seps.pop(0)

                self.words[curr_size].append(line.strip())

                curr_line += 1

    def correct(self, word1: str) -> str:
        best_dist = float('inf')
        best_word = None

        for size in range(max(0, len(word1)-1),
                          min(self.largest_word_len, len(word1)+2)):
            for match in self.words[size]:
                dist = lev_dis(word1, match)

                if dist < best_dist:
                    if dist == 0:  # Exit immediately, the word has been found.
                        return match

                    best_dist = dist
                    best_word = match

        return best_word
