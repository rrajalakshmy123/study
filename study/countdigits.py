class Solution:
    def countDigit(self, n):
        count=1
        while(n>0):
            n=n//10
            count=count+1
        return count
    
if __name__ == "__main__":
    n=12345
    obj=Solution()
    result=obj.countDigit(n)
    print(result)