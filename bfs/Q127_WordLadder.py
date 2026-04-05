import string
from collections import deque
from typing import Iterator, List


class Solution:


    def ladderLength_bidirectionalBFS(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # same time complexity O(m^2 * n) as one direction BFS
        # the number of nodes to visit is about half.
        dictionary = set(wordList)

        def getNeighbors(word: str) -> Iterator[str]:
            for i in range(len(word)):
                for newChar in string.ascii_lowercase:
                    if newChar == word[i]:
                        continue
                    newWord = word[:i] + newChar + word[i +1:]
                    if newWord in dictionary:
                        yield newWord

        if endWord not in dictionary:
            return 0
        front = {beginWord}
        front_seen = {beginWord}
        back = {endWord}
        back_seen = {endWord}
        step = 1
        while front and back:
            if len(front) > len(back):
                front, back = back, front
                front_seen, back_seen = back_seen, front_seen
            front_next = set()
            for word in front:
                # visit
                if word in back_seen:
                    return step
                for neighbor in getNeighbors(word):
                    if neighbor not in front_seen:
                        front_next.add(neighbor)
                        front_seen.add(neighbor)
            front = front_next
            step += 1
        return 0  # never found a path


    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Can I assume endWord in wordList?
        # Assume there must be a path from beginWord to endWord?  No!
        # Assume word made of lower case English letters?
        # Duplicates in wordList?
        # beginWord and endWord have same length?
        # endWord must be in wordList?
        # will beginWord be the same as endWord?
        # will all words have the same length?

        # Time complexity: O(m^2*n). It takes O(n) time to traverse with BFS, where n is the number of words in wordsList.
        # At the each word, we need find all its O(26 * m) neighbors, and it takes O(m) time to construct a neighbor, where m is length of
        # the word. Hence overall, the time compleixty is O(m^2 * n)
        def getNeighbors(word: str) -> Iterator[str]:
            l = list(word)
            for i, char in enumerate(l):
                for newChar in string.ascii_lowercase:
                    if newChar == char:
                        continue
                    l[i] = newChar
                    yield "".join(l)
                l[i] = char

        dictionary = set(wordList)
        if endWord not in dictionary:
            return 0
        seen = set()
        queue = deque()
        queue.append(beginWord)
        seen.add(beginWord)
        level = 1
        while len(queue) > 0:
            size = len(queue)
            for i in range(size):
                word = queue.popleft()
                if word == endWord:
                    return level
                for neighbor in getNeighbors(word):
                    if neighbor not in seen and neighbor in dictionary:
                        queue.append(neighbor)
                        seen.add(neighbor)
            level += 1

        return 0  # never found a path
if __name__ == '__main__':
    print(Solution().ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
