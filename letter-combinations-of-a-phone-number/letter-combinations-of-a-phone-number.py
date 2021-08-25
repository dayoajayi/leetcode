class Solution:       
    def letterCombinations(self, digits: str) -> List[str]:
        KEYPAD = { 
                 "0": ["0"],
                 "1": ["1"],
                 "2": ["a", "b", "c"],
                 "3": ["d", "e", "f"],
                 "4": ["g", "h", "i"],
                 "5": ["j", "k", "l"],
                 "6": ["m", "n", "o"],
                 "7": ["p", "q", "r", "s"],
                 "8": ["t", "u", "v"],
                 "9": ["w", "x", "y", "z"]
                }
        allCombos = []
        currentCombo = ["0"] * len(digits)
        
        def comboHelper(idx):
            # base case
            if idx == len(digits):
                combo = "".join(currentCombo)
                allCombos.append(combo)
            # do work
            else:
                digit = digits[idx]
                letters = KEYPAD[digit]
                for letter in letters:
                    currentCombo[idx] = letter
                    comboHelper(idx + 1)
        
        if digits == "": return []
        comboHelper(0)
        return allCombos