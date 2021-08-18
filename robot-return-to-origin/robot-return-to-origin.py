class Solution:
    def judgeCircle(self, moves: str) -> bool:
        UD = 0
        LR = 0
        
        for i in range(len(moves)):
            if moves[i] == "U": 
                UD = UD+1
            elif moves[i] == "D": 
                UD = UD-1
            elif moves[i] == "L": 
                LR = LR-1
            elif moves[i] == "R": 
                LR = LR+1
                
        return UD == 0 and LR == 0