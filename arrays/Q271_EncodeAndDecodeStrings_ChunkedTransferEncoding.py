from typing import List


class Codec:
    # Chunk Transfer Encoding is a much more straight forward way of encoding than escaping.
    # And it is easy to implement.
    # It is used in the HTTP protocol: https://en.wikipedia.org/wiki/Chunked_transfer_encoding
    # <chunk 1 size>CRLF<chunk 1 content>CRLF<chunk 2 size>CRLF<chunk 2 content>
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        l = []
        delimiter = '#'
        for s in strs:
            size = len(s)
            element = "".join([str(size), delimiter, s])
            l.append(element)
        return "".join(l)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        delimiter = '#'
        l = []
        p = 0
        while p < len(s): # works for empty list too because s would an empty string in such case
            q = s.find(delimiter, p) # look for next delimiter, starting from p
            size = int(s[p:q])
            element = s[q + 1: q + 1 + size]
            l.append(element)
            p = q + 1 + size
        return l


# test cases:
# []
# ["", ""]
# ["0#", "1#a", "#"]

if __name__ == '__main__':
    for l in [["hello", "world"], ["", "0#", "1#a"]]:
        codec = Codec()
        encoded = codec.encode(l)
        print(encoded)
        decoded = codec.decode(encoded)
        print(decoded)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))