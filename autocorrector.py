from Levenshtein import distance as lev_dis


class Autocorrector:

    def __init__(self, dict_path: str):
        self.dict_path = dict_path
        self.words = []
        with open(dict_path, 'r') as fin:
            for line in fin:
                self.words.append(line.replace('\n', ''))

    def correct(self, word1: str) -> str:
        distances = []
        for word in self.words:
            distances.append(lev_dis(word1, word))
        return self.words[distances.index(min(distances))]
