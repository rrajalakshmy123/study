from typing import List

def twosum(nums: List[int], target: int):
    store={}
    for i,num in enumerate(nums):
        value= target-num
        if(value in store):
            return store[value], i
        store[num]=i
        print(store)
    
    
if __name__ == "__main__":
    
    print(twosum([2,7,11,15],26))

