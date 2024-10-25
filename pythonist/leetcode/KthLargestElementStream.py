import heapq
from typing import List
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)[-k::]
    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

def main():
    K = KthLargest(3, [4, 5, 8, 2])
    print(K.add(3))

    print(K.add(5))
    print(K.add(10))
    print(K.nums)

    #print('res', carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
    #print('res', inorderTraversal([1,2,3,4,5,null,8,null,null,6,7,9]))



if __name__ == "__main__":
    main()
