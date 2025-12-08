
arr=[2,0,1,0,0,4,5]

[3, 1, 4, 5, 2, 0, 0]

n=len(arr)

def movezeroes(arr):
    pos=0
    for i in range(n):
        if(arr[i]!=0):
            temp=arr[pos]
            arr[pos]=arr[i]
            arr[i]=temp
            pos=pos+1
    # while pos < n:
    #     arr[pos] = 0
    #     pos += 1      
    return arr
    
if __name__ == "__main__":
    array=movezeroes(arr)
    print(array)