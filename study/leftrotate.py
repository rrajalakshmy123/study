from ast import main 
array=[2,3,4,5,6]
def leftrotate(array):
    first=array[0]
    n=len(array)
    for i in range(1,n):
        array[i-1]=array[i]
    array[n-1]=first
    return array

if __name__ == "__main__":
    array=leftrotate(array)
    print (array)
    