import heapq
from collections import defaultdict
class SeatManager:

    def __init__(self, n: int):
        self.seats = list(range(1, n+1))

        #self.seats = dict.fromkeys(list(range(1, n+1)), False)
        # self.reserv = []

    def reserve(self) -> int:
        return heapq.heappop(self.seats)

        # for idx in sorted(self.seats):
        #     if self.seats[idx] == False:
        #         self.seats[idx] = True
        #         return idx
    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.seats, seatNumber)
        # self.seats[seatNumber] = False

def main():
    s = SeatManager(5)
    s.reserve()
    s.reserve()
    s.unreserve(1)
    print(s.seats)
    #print('res', carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
    #print('res', inorderTraversal([1,2,3,4,5,null,8,null,null,6,7,9]))



if __name__ == "__main__":
    main()
# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)