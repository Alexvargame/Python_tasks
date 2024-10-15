# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class MountainArray(object):
   def get(self, index):
       return self[index]

   def length(self):
       return len(self)

class Solution:

    def find_peak(self):
        l = 1
        r = self.arr_len - 2

        while l <= r:
            mid = (l + r) // 2
            val_l = self.arr.get(mid-1)
            val_mid = self.arr.get(mid)
            val_r = self.arr.get(mid + 1)

            if val_l <= val_mid <= val_r:
                l = mid + 1
            elif val_l > val_mid > val_r:
                r = mid - 1
            else:
                return mid



    def bin_search(self, start, end, target, asc=True):
        l = start
        r = end
        while l <= r:
            mid = (l+r) // 2
            val_mid = self.arr.get(mid)
            if val_mid > target:
                if asc:
                    r = mid - 1
                else:
                    l = mid + 1
            elif val_mid < target:
                if asc:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                return mid


    def findMountainArray(self, target, mountain_arr ):
        self.arr = mountain_arr
        self.arr_len = mountain_arr.length()

        peak = self.find_peak()
        result = self.bin_search(0, peak, target)
        if result is not None:
            return result
        result = self.bin_search(peak, self.arr_len-1, target, False)
        if result is not None:
            return result
        return -1



def main():
    s = Solution()
    mountain_arr = MountainArray()
    #print('res', carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
    print('res', s.findMountainArray(3, [1,2,3,4,5,3,1]))



if __name__ == "__main__":
    main()
