from typing import List


class Solution:
    # The high level idea is that for each machine, find upper bound of units, then perform binary search between
    # [lower_bound, upper_bound] to find the max units that machine can make within budge. Then find the max among
    # all machines.
    # When finding the upper bound, we start from 1 unit, and keep doubling the number of units until exceeding the
    # budget.
    # Each time calculating cost takes O(n) where n is the types of metal. Suppose the answer is a, finding upper bound
    # takes O(log(a) * n) time for one machine. Binary search takes O(log(a) * n) time for one machine. Overall time
    # complexity is O(log(a) * n * k) because there are k machines.
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int],
                          cost: List[int]) -> int:
        # Assuming valid input: cost[i] > 0

        def calculate_cost(machine, units):
            total = 0
            for metal in range(n):
                units_to_buy = max(composition[machine][metal] * units - stock[metal], 0)
                total += units_to_buy * cost[metal]
            return total

        def find_upper_bound(machine):
            units = 1
            while True:
                total = calculate_cost(machine, units)
                if total > budget:
                    return units
                units *= 2

        def binary_search(machine, upper_bound, lower_bound):
            start = lower_bound
            end = upper_bound
            while start + 1 < end:
                mid = (start + end) // 2
                total = calculate_cost(machine, mid)
                if total <= budget:
                    start = mid
                else:
                    end = mid
            if calculate_cost(machine, end) <= budget:
                return end
            return start

        max_units = 0
        for machine in range(k):
            upper_bound = find_upper_bound(machine)
            lower_bound = upper_bound // 2
            units = binary_search(machine, upper_bound, lower_bound)
            max_units = max(max_units, units)
        return max_units