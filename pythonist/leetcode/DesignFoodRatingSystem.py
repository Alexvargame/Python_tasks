from collections import defaultdict
import bisect

class FoodRatings(object):

    def __init__(self, foods, cuisines, ratings):
        """
        :type foods: List[str]
        :type cuisines: List[str]
        :type ratings: List[int]
        """
        self.foods =  {}
        self.cuisines =  defaultdict(list)
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.foods[food] = (cuisine, rating)
            bisect.insort(self.cuisines[cuisine], (-rating, food))




    def changeRating(self, food, newRating):
        """
        :type food: str
        :type newRating: int
        :rtype: None
        """
        cuisine, rating = self.foods[food]
        idx = bisect.bisect_left(self.cuisines[cuisine], (-rating, food))
        self.cuisines[cuisine].pop(idx)
        bisect.insort(self.cuisines[cuisine], (-newRating, food))
        self.foods[food] = (cuisine, newRating)


    def highestRated(self, cuisine):
        """
        :type cuisine: str
        :rtype: str
        """
        return self.cuisines[cuisine][0][1]

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)

def main():
    #print('res', carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
    #print('res', merge([[1,3],[2,6],[8,10],[15,18]]))



if __name__ == "__main__":
    main()
