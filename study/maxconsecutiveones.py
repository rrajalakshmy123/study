arr = [1, 1, 0, 0, 1, 1, 1, 0]

n=len(arr)

def maxones(arr):
    count1=0
    count2=0
    for i in range(n):
        if(arr[i]==1):
            count1=count1+1
        if(arr[i]!=1):
            count2=max(count2, count1)
            count1=0      
    return count2

if __name__ == "__main__":
    value=maxones(arr)
    print(value)