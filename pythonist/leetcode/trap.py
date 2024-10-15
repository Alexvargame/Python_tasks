def trap(height):
   if not height:
       return 0
   l = 0
   r = len(height) -1
   maxL = height[l]
   maxR = height[r]
   res = 0

   while l < r:
       if maxL < maxR:
           l += 1
           maxL = max(maxL, height[l])
           res += maxL - height[l]
       else:
           r -= 1
           maxR =max(maxR, height[r])
           res += maxR - height[r]


   return res

def main():
    #print('res', carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
    print('res', trap([0,1,0,2,1,0,1,3,2,1,2,1]))



if __name__ == "__main__":
    main()
