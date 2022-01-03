class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        numberOfProvinces = 0
        
        def dfs(city):
            visited.add(city)
            for neighbor in range(len(isConnected)):
                if isConnected[city][neighbor] and neighbor not in visited:
                    dfs(neighbor)
        
        for city in range(len(isConnected)):
            if city not in visited:
                dfs(city)
                numberOfProvinces += 1
        
        
        return numberOfProvinces
        

        
        
'''
Time: O(N^2)
Space: O(N)


isConnected = [
                [1,1,0],
                [1,1,0],
                [0,0,1]
            ]


'''