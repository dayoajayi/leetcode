from typing import List
from collections import Counter
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = defaultdict(list)
        output = []
        
        # convert each string in the list to its own list and sort it 
        # use the sorted anagram as key, and add the anagrams as values
        for word in strs:
            key = "".join(sorted(list(word)))
            lookup[key].append(word)
        
        # generate the output by looping through the lookup dictionary
        for l in lookup.values():
            output.append(l)

        return output     
                 
s = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]

print(s.groupAnagrams(strs))


'''
https://leetcode.com/problems/group-anagrams/

Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of 
a different word or phrase, typically using all the original letters exactly once.
'''
