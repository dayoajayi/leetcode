class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]: 
        result = []
	
        for i in [1,2,3]:
            for j in [i+1, i+2, i+3]:
                for k in [j+1, j+2, j+3]:
                    if k >= len(s):
                        continue
                    segment1 = s[:i]
                    segment2 = s[i:j]
                    segment3 = s[j:k]
                    segment4 = s[k:]
                    if self.checkValidSegments([segment1,segment2, segment3, segment4]):
                        newAddress = f"{segment1}.{segment2}.{segment3}.{segment4}"
                        result.append(newAddress)
        return result

    def checkValidSegments(self, segmentsList):
        for s in segmentsList:
            if s[0] == "0" and s != "0":
                 return False
            if int(s) > 255:
                 return False
        return True