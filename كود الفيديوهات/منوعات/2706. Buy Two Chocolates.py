class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        def find_and_delete_min(prices):
            mn = 101
            mn_index = -1
            for index, price in enumerate(prices):
                if price < mn:
                    mn = price
                    mn_index = index
            prices[mn_index] = 101
            return mn
        
        min1 = find_and_delete_min(prices)
        min2 = find_and_delete_min(prices)

        if money-min1-min2 > -1:
            return money-min1-min2
        
        return money