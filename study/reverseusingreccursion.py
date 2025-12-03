from ast import main

def reversearray(arr, start, end):
    if(start>end):
        return arr
    else:
        arr[start],arr[end]=arr[end],arr[start]
        start=start+1
        end=end-1
        reversearray(arr, start, end)
        return arr


if __name__ == "__main__":
    arr=reversearray([4,5,6,7],0,3)
    print(arr)
