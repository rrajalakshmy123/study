from ast import main

array =[1,2,5,5,5]

def checksorted(arrayforchecking):
    first=array[0]
    for i in range(1,len(array)):
        if array[i]>=first:
            first=array[i]
            i=i+1
        else :
            print("array is not sorted")
            return
    print("array is sorted")

if __name__ == "__main__":

    checksorted(array)