array=[3, 4, 1, 5, 3, -5]
654321
345612
       
k=8
n=len(array)
def reverse(array,i,j):
    while i < j:
        array[i], array[j-1] = array[j-1], array[i]
        i += 1
        j -= 1
    return array

def leftrotatebyk(array,k):
        k =k%n
        reverse(array,0,k)
        reverse(array,k,n)
        reverse(array,0,n)
        return array


if __name__ == "__main__":
    array=leftrotatebyk(array,k)
    print (array)