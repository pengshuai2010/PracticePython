from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # will there be 0 speed? negative speed. distance?
        cars = list(zip(position, speed))
        #
        # Car A is not able to catch up with Car B if remaining time for Car A is greater than the remaining time of Car B
        # Edge case to clarify: two cars has the same position, but different speed, i.e. different remaining
        # time. Will they move apart, or will one block the other causing them to form a fleet? The implication is
        # how we shold sort the cars.
        #
        # (position, speed)
        # the closer to the target, the higher the speed, the earlier to reach the target.
        # the implication of this order is that two cars at the same position but different speed will drift away,
        # i.e. not form a fleet.
        cars.sort(reverse=True)
        # Consider [(0, 5), (2, 3), (4, 6)]. (2, 3) will catch up with (4, 6), then both will travel at
        # the speed of (4, 6). So (4, 6) should be the "representative" of the fleet.
        # When deciding if (0, 5) will catch up with fleet, we should compare (0, 5) with the the
        # "representative" (4, 6).
        # The algorithm is to fo from right to left, if the car to the left is able to catch up with the
        # current representative, we discard the the car to the left, and keep the current representativet; otherwise we increase the fleet count by 1, and discard the current representative, and use
        # use the car to the left as representative of the new fleet.
        # This is suitable to solve with stack.
        stack = []
        for position, speed in cars:
            time = (target - position) / speed
            if len(stack) == 0:
                stack.append(time)
            else:
                prev_time = stack[-1]
                if time > prev_time: # not able to catch up
                    stack.append(time)
        return len(stack)