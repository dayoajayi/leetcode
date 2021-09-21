class Solution:
    def __init__(self):
        self.result = ""
        self.carry = 0

    def processRest(self, remst):
        start = len(remst) - 1
        print (f"{remst}")
        while start >= 0:
            tempSum = int(remst[start]) + self.carry
            
            self.result = str(tempSum % 10) + self.result
            self.carry = tempSum // 10
            start -= 1
            
    def addStrings(self, num1: str, num2: str) -> str:
        idx1, idx2 = len(num1) - 1, len(num2) - 1
        remst1 = ""        
        # shortCarry
        while idx1 >= 0 and idx2 >= 0:
            tempSum = int(num1[idx1]) + int(num2[idx2]) + self.carry
            self.result = str(tempSum % 10) + self.result
            self.carry = tempSum // 10
            
            idx1 -= 1
            idx2 -= 1
        
        idx1 += 1
        idx2 += 1
        
        if idx1 > idx2:
            remst = num1[:idx1]
            self.processRest(remst)
        elif idx1 < idx2:
            remst = num2[:idx2]
            self.processRest(remst)
    
        #print (f"{self.carry},{self.result}")
        return str(int(f"{self.carry}{self.result}"))
        
            
        
        


'''
get the length of each number
ones
tens
hundreds
carry
'''