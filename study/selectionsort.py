def selectionsort(arr):
    for i in range(len(arr)):
        min=i
        for j in range (i+1,len(arr)):
            if(arr[j]<arr[min]):
                min = j
        arr[i], arr[min] = arr[min], arr[i]
        print(arr)
    return arr
def bubblesort(arr):
    for i in range (len(arr)):
        swap=False
        for j in range(i+1,len(arr)):
            if(arr[j]<arr[i]):
                arr[i], arr[j] = arr[j], arr[i]
                swap=True
        if not swap:
            break
    return arr


if __name__ == "__main__":
    sortedarr=selectionsort([78,26,90,30,100,1])
    sortedarrbubble=bubblesort([78,26,90,30,100,1])
    print(sortedarr)
    print(sortedarrbubble)
