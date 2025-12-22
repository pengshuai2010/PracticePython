from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        l = []
        for s in strs:
            builder = []
            for ch in s:
                if ch == '\\':
                    builder.append("\\\\")
                elif ch == '"':
                    builder.append('\\"')
                else:
                    builder.append(ch)
            element = "".join(builder)
            l.append(element)
        builder = []
        for element in l:
            builder.append("".join(['"', element, '"']))
        return "".join(["[", ', '.join(builder), "]"])

# test cases:
# ["", ""]
# ["\"", "\\", "ab"]


    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        l = []
        builder = []
        index = 0
        decoding_mode = False
        while index < len(s):
            current_char = s[index]
            if current_char == '"':
                if decoding_mode:
                    l.append("".join(builder))
                    builder = []
                decoding_mode = not decoding_mode
                index += 1
                continue
            if decoding_mode:
                if current_char == '\\':
                    next_char = s[index + 1] # we should never encounter a single slash
                    if next_char == '\\':
                        builder.append('\\')
                        index += 1
                    elif next_char == '"':
                        builder.append('"')
                        index += 1
                    else:
                        raise ValueError() # we should never encounter a single slash
                else:
                    builder.append(current_char)
            index += 1
        return l

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))