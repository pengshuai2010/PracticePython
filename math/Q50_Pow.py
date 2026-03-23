class Solution:
    def myPow(self, x: float, n: int) -> float:
        # what is the range of x and n?
        is_negative = n < 0
        if n < 0:
            n = -n
            x = 1 / x

        def pow_recursive(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x
            if n % 2 == 0:
                answer = pow_recursive(x, n // 2)
                return answer * answer
            return x * pow_recursive(x, n - 1)

        return pow_recursive(x, n)

    def myPow_iterative(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        is_negative = n < 0
        if n < 0:
            n = -n
        answer = 1
        power = x
        while n > 0:
            if n % 2 == 1:
                answer *= power
            power *= power
            n = n // 2
        if is_negative:
            answer = 1 / answer
        return answer

# n = 10, 5, 2, 1, 0
# power = x^8
# answer = 1 * x^2 * x^8