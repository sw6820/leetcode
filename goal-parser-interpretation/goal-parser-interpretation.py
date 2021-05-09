class Solution:
    def interpret(self, command: str) -> str:
        s,idx='',0
        while idx<len(command):
            if command[idx]=='G':
                s+='G'
                idx+=1
            else:
                if command[idx+1]==')':
                    s+='o'
                    idx+=2
                else:
                    s+='al'
                    idx+=4
        return s