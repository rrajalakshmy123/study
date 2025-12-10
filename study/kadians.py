nums = [2, 3, -5, -2, 7, -4]
Output = 15

def kadians(nums):
    sum=0
    maxsum=float('-inf')
    n=len(nums)
    start=0
    end=0
    for i in range(n):
        sum=sum+nums[i]
        if(sum<0):
            sum=0
            start=i+1
        if(sum>maxsum):
            maxsum=sum
            end=i
    print(start,end)
    return maxsum, start, end

if __name__ == "__main__":

    sum, start, end = kadians(nums)
    print(sum)
    print("Subarray:", nums[start:end+1])