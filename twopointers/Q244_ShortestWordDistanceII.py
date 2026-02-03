from collections import defaultdict
import math
from typing import List


class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self._indices = defaultdict(list)
        for i, word in enumerate(wordsDict):
            self._indices[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        # will word1 and word2 be distinct? 
        # word1 and word2 in the list? 
        indices1 = self._indices[word1]
        indices2 = self._indices[word2]
        p1 = 0
        p2 = 0
        min_distance = math.inf
        while p1 < len(indices1) and p2 < len(indices2):
            distance = abs(indices1[p1] - indices2[p2])
            min_distance = min(min_distance, distance)
            if indices1[p1] < indices2[p2]:
                p1 += 1
            else:
                p2 += 1
        return min_distance
