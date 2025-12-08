arr=[0, 2, 3, 1, 4]

n=len(arr)

def missingnumber(arr):
    s=0
    sum=n*(n+1)/2    
    for i in range(n):
        s=s+arr[i]
    value=sum-s

    return int(value)
    
if __name__ == "__main__":
    value=missingnumber(arr)
    print(value)