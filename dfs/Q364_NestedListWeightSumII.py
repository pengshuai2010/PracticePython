class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        def helper(nestedInteger: NestedInteger, depth) -> tuple[int, int, int]:
            if nestedInteger.isInteger():
                value = nestedInteger.getInteger()
                return (value, depth * value, depth)
            total = 0
            total_weighted = 0
            max_depth = depth
            for item in nestedInteger.getList():
                result = helper(item, depth + 1)
                total += result[0]
                total_weighted += result[1]
                max_depth = max(max_depth, result[2])
            return (total, total_weighted, max_depth)

        total = 0
        total_weighted = 0
        max_depth = 1
        for item in nestedList:
            result = helper(item, 1)
            total += result[0]
            total_weighted += result[1]
            max_depth = max(max_depth, result[2])

        return total * (max_depth + 1) - total_weighted