def solution(s):
   l = len(s); ans=l
   for i in range(1, (l//2)+1):
       prev=s[:i];j=i;flag=1;tl=l
       while 1:
           if j+i > l: break
           if prev == s[j:j+i]:
               flag+=1; tl-=i
           else:
               if flag>1: tl+=len(str(flag))
               flag=1
               prev=s[j:j+i]
           j+=i
       if flag>1: tl+=len(str(flag))
       ans = min(ans, tl)
   return ans

s = "aabbaccc"

print(solution(s))