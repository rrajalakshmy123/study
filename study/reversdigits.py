class Solution:
    def reverseNumber(self, n):
        sum=0
        while(n>0):
            digit=n%10
            sum =sum*10+digit
            n=n//10
        return sum

if __name__ == "__main__":
    n=12345
    obj=Solution()
    result=obj.reverseNumber(n)
    print(result)
    