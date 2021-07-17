class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i in ['(','{','[']:stack.append(i)
            else:
                if stack:
                    if i==')':
                        if stack.pop()!='(': return False
                    elif i=='}':
                        if stack.pop()!='{': return False
                    else:
                        if stack.pop()!='[': return False
                else: return False
        return False if stack else True