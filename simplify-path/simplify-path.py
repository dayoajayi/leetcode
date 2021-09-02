class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        for segment in path.split("/"):
            if stack and segment == "..":
                stack.pop()
            elif segment not in ["", ".",".."]:
                stack.append(segment)
        
        return "/" + "/".join(stack)        