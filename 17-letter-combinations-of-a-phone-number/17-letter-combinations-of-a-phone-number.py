class Solution:
    def letterCombinations(self, digits: str) -> List[str]:        
        KEYPAD = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        def comboHelper(idx):
            if idx == len(digits):
                combo = "".join(currentCombo)
                allCombos.append(combo)
            else:
                digit = digits[idx]
                letters = KEYPAD[digit]
                for letter in letters:
                    currentCombo[idx] = letter
                    comboHelper(idx + 1)                   
        
        allCombos = []
        currentCombo = ["0"] * len(digits)
            
        if digits == "": return []
        comboHelper(0)
        return allCombos
             
'''
T: O(4^N)
S: O(4^N)
'''