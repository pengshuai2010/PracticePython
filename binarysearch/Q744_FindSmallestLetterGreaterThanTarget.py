class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # will letters be empty?
        # all lower case English letters?
        # if ord(letters[-1]) <= ord(target):
        #     return  letters[0]

        s = 0
        e = len(letters) - 1
        while s + 1 < e:
            mid = (s + e) // 2
            if ord(letters[mid]) <= ord(target):
                s = mid
            else:
                e = mid
        # Be careful of the case where target is outside of the range of letters
        # e.g. [b, c, e], target = a, then eventually [b, c] are all greater than a.
        if ord(letters[s]) > ord(target):
            return letters[s]
        # will it ever happen that e moved to an element that ord(letter[e]) < ord(target)? No, because
        # e moves to mid only if ord(letters[mid]) > ord(target).
        # The only reason target is outside of range [e, s] is that target is outside of the range of the array.
        if ord(letters[e]) <= ord(target):
            return letters[0]
        return letters[e]

# test
# [a, b, c] target = c
# [a, b, c], target = b
# [a, c, e], target = b
# [b, c, e], target = a