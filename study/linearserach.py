arr=[2,4,5,1,1,3]
target=1
def linearserach(arr,target):
    for i in range(len(arr)):
        if(target==arr[i]):
            return i

if __name__ == "__main__":
    pos=linearserach(arr,target)
    print(pos)


