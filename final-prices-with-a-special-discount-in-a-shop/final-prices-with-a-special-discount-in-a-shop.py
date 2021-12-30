class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        '''
                       
        prices = [8,4,6,2,3]
        output = [4,2,4,2,3]                                    
        
        '''
        stack = []
        
        for i in range(len(prices)):
            currentPrice = prices[i]
            while stack and currentPrice <= prices[stack[-1]]:
                idx = stack.pop()
                prices[idx] -= prices[i]
                
            stack.append(i)
        return prices