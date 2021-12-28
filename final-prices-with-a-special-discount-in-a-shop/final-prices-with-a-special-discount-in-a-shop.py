class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        
        for i in range(len(prices)):
            currentPrice = prices[i]
            while stack and currentPrice <= prices[stack[-1]]:
                idx = stack.pop()
                prices[idx] -= currentPrice
                
            stack.append(i)
                
        return prices
        
    
    
    
    '''
    WHY DOES THIS NOT WORK??
    
    def finalPrices(self, prices: List[int]) -> List[int]:
        output = []
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j] < prices[i]:
                    discount = prices[j]
                    output.append(prices[i] - prices[j])
                    break
                else:
                    output.append(prices[j])
        return output
        
        
    '''