class Solution:
    def maximumTime(self, time: str) -> str:
        t=''
        if time[0]=='?':            
            t+='2'if time[1]=='?' or int(time[1])<4 else '1'
        else: t+=time[0]
        if time[1]=='?':
            t+='3' if t[0]=='2' else '9'
        else: t+=time[1]
        t+=':'
        t+='5'if time[3]=='?'else time[3]
        t+='9'if time[4]=='?'else time[4]
        return t
        
            
            