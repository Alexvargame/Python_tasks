def maxProfit(prices):
     """
        :type prices: List[int]
        :rtype: int
     """
     max_profit = 0
     buy = prices[0]
     sell = 0

     for i in range(1, len(prices)):
         print('BEG', prices[i], buy, sell, max_profit)
         if prices[i] > buy:
             sell = prices[i]
             max_profit = max(max_profit,sell - buy)#prices[i]
             #sell = prices[i]
         else:
             buy = prices[i]
         print('END', prices[i], buy, sell, max_profit)
     return max_profit


     # print(sorted(prices)[::-1])
     # #[[prices[i]-prices[j] for j in range(len(prices))] for i in range(len(prices))]
     # print(max([max([j-prices[i] for j in prices[i:]]) for i in range(len(prices))]))
     # print([max(prices[i:]) for i in range(len(prices))])

def main():
    print('res', maxProfit([7,1,5,3,6,4]))



if __name__ == "__main__":
    main()
