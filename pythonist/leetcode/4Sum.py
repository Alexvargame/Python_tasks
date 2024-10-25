class Solution:

    def two_sum(self, start, target):
        nums = self.nums
        l = start
        r = len(nums) - 1

        while l < r:
            l_value = nums[l]
            r_value = nums[r]
            value = l_value + r_value
            if value < target:
                l += 1
            elif value > target:
                r -= 1
            else:
                self.results.append(self.prefix + [l_value, r_value])
                l += 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1

    def k_sum(self, k, start, target):
        if k == 2:
            self.two_sum(start, target)
            return
        nums = self.nums
        for idx in range(start, len(nums) - k + 1):
            if idx > start and nums[idx] == nums[idx - 1]:
                continue
            value = nums[idx]
            self.prefix.append(value)
            self.k_sum(k - 1, idx + 1, target - value)
            self.prefix.pop()


    def fourSum(self, nums, target):
        nums.sort()
        self.nums = nums
        self.prefix = []
        self.results = []
        self.k_sum(5, 0, target)
        return self.results

def main():
    #print('res', fourSum([1,0,-1,0,-2,2], 0))
    s = Solution()
    print(s.fourSum([2,2,2,2,2,2], 10))



if __name__ == "__main__":
    main()
