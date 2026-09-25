class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1=="0" or num2=="0":
            return "0"
        n=len(num1)
        m=len(num2)
        res=[0]*(n+m)
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                a=ord(num1[i])-ord('0')
                b=ord(num2[j])-ord('0')
                res[i+j+1]+=a*b
        for i in range(n+m-1,0,-1):
            res[i-1]+=res[i]//10
            res[i]%=10
        ans=""
        for x in res:
            if ans=="" and x==0:
                continue
            ans += chr(x + ord('0'))
        return ans


       
        

        