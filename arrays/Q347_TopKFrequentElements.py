import collections
from collections import Counter
import heapq
from typing import List


class Solution:
    # There is also a quickselect algorithm that can reach O(n) time complexity.
    # With bucket sort we can also reach O(n) time complexity and bucket sort is a lot easier to implement
    # in an interview.

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # clarifying questions: is k <= len(nums) ? k > 0? Is k guaranteed to be less than m, the number of
        # unique numbers?
        # Time complexity: O(n) for iterating over the list, O(m * log(k)) for putting in and taking out m
        # elements in a min heap of size k, where m is the number of unique numbers, and m <= n.
        counter = Counter(nums)
        min_heap = []
        for num, frequency in counter.items():
            # There is no need to compare current item with the top of the min heap and then decide whether to
            # add the item, just add the item and then do a heap pop if heap size aleady greater than k

            # if len(min_heap) < k:
            #     # (frequency, num) because we want to sort by frequency
            #     heapq.heappush(min_heap, (frequency, num))
            # else:
            #     # current_frequency = min_heap[0][0]
            #     # if frequency > current_frequency:
            #     #     heapq.heappop(min_heap)
            #     #     heapq.heappush(min_heap, (frequency, num))
            #     heapq.heappush(min_heap, (frequency, num))
            #     heapq.heappop(min_heap)

            # (frequency, num) because we want to sort by frequency
            heapq.heappush(min_heap, (frequency, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return [num for frequency, num in min_heap]

    def topKFrequent_maxHeap(self, nums: List[int], k: int) -> List[int]:
        # time complexity O(n) for iterating through the list, O(m) for heapify, O(k * log(m)) for taking
        # out the k largest elements in the max heap, where m is the number of unique numbers and m <= n.
        # When m >> k, O(k * log(m)) is less than O(m * log(k)).
        # However, when your algorithm need to work with a stream of elements, you would have to use min heap
        # solution.
        counter = Counter(nums)
        # heapq.nlargest(n, iterable, key=None)
        # key is the function to get a key for comparison
        # return heapq.nlargest(k, counter.keys(), counter.get)
        l = [(frequency, num) for num, frequency in counter.items()]
        return [num for frequency, num in heapq.nlargest(k, l)]

    def topKFrequent_bucketsort(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        bucket = collections.defaultdict(list)
        for number, count in counter.items():
            bucket[count].append(number)
        top_k = []
        for count in reversed(range(len(nums) + 1)): # range(n) doesn't include n
            if len(top_k) >= k:
                break
            if count in bucket:
                top_k.extend(bucket[count])
        return top_k[:k]

if __name__ == '__main__':
    for nums, k in [([1,1,1,2,2,3], 2), ([1], 1)]:
        print(Solution().topKFrequent(nums, k))