class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # will digits be invalid? e.g. empty? leading zero?
        result = []
        carry = 1
        for i in reversed(range(len(digits))):
            number = digits[i] + carry
            carry = number // 10
            digit = number % 10
            result.append(digit)
        if carry > 0:
            result.append(carry)
        return list(reversed(result))

# [0]
# [9]
# [9, 9]
# [1, 9]