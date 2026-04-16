class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        _map = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        
        for i in s:
            if i in _map:
                if stack and stack[-1] == _map[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
                
        return True if not stack else False