import collections
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # will there be divided by 0 error
        # what are the operands? Do we need to handle fractions?
        # express guaranteed valid? e.g. single operand?
        # will there be overflow?
        stack = collections.deque()
        # operators = {'+', '-', '*', '/'}
        operators = "+-*/" # Pythonic way
        for token in tokens:
            if token in operators:
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = self._calculate(token, operand1, operand2)
                stack.append(result)
            else:
                stack.append(int(token))
        return stack.pop()

    def _calculate(self, operator: str, operand1: int, operand2: int) -> int:
        result = 0
        if operator == '+':
            result = operand1 + operand2
        elif operator == '-':
            result = operand1 - operand2
        elif operator == '*':
            result = operand1 * operand2
        elif operator == '/':
            # int() truncates toward zero
            # the integer division operator // will round down <=> math.floor()
            result = int(operand1 / operand2)
        else:
            raise ValueError("unsupported operator")
        return result

    # use match case
    # def _calculate(self, operator: str, operand1: int, operand2: int) -> int:
    #     result = 0
    #     match operator:
    #         case '+':
    #             result = operand1 + operand2
    #         case '-':
    #             result = operand1 - operand2
    #         case '*':
    #             result = operand1 * operand2
    #         case '/':
    #         # int() truncates toward zero
    #         # the integer division operator // will round down <=> math.floor()
    #             result = int(operand1 / operand2)
    #         case _:
    #             raise ValueError("unsupported operator")
    #     return result