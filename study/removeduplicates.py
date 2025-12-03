from ast import main

array =[1,2,5,5,5]

def removeduplicates(arrayforchecking):
    i=0
    while(i<len(arrayforchecking)):
        j=i+1
        if array[i]==array[j] :
           array.pop(j)
        else :
            j=j+1
        i=i+1
if __name__ == "__main__":

    removeduplicates(array)