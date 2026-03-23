from typing import List


class Solution:
    def findRepeatedDnaSequences_hash(self, s: str) -> List[str]:
        # will len(s) < 10?
        sequences = set()
        repeated_sequences = set()
        k = 10
        for i in range (len(s) - k + 1):
            sequence = s[i: i + k]
            if sequence in sequences:
                repeated_sequences.add(sequence)
            else:
                sequences.add(sequence)
        return list(repeated_sequences)

    # Building hash incrementally only takes constant time ( not related to k)
    # Time complexity is O(n - k) + O(m*k) where m is the number of repeated sequences.
    # Space complexity is O(n - k). The hash of each sequence is hold in an integer. And the number of bits is  k*2.
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # will len(s) < 10?
        seen = set()
        repeated_sequences = set()

        number_map = {"A": 0, "C": 1, "G": 2, "T": 3}
        k = 10
        bitmask = (1 << (k * 2)) - 1  # Each character takes up 2 bits.

        def build_initial_hash(sequence):
            value = 0
            for char in sequence:
                value <<= 2
                value |= number_map[char]
            return value

        def build_incremental_hash(prev_value, char):
            value = prev_value << 2
            value &= bitmask
            value |= number_map[char]
            return value

        hash_value = build_initial_hash(s[0: k])
        seen.add(hash_value)
        for i in range(1, len(s) - k + 1):
            hash_value = build_incremental_hash(hash_value, s[i + k - 1])
            if hash_value in seen:
                repeated_sequences.add(s[i: i + k])
            else:
                seen.add(hash_value)
        return list(repeated_sequences)

if __name__ == '__main__':
    Solution().findRepeatedDnaSequences_bitmanipulation("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")