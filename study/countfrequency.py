def countfrequency(arr):
    store={}
    for i,v in enumerate(arr):
        if(v in store):
            store[v]=store[v]+1
        else:
            store[v]=1
    return store
if __name__ == "__main__":
    out=(countfrequency([5,5,5,3,4,6]))
    print(max(out.values()))
  
    result = []
    for key, value in out.items():
        result.append([key, value])
        
    print(result)
    # {'5': 3, '3': 1, '4': 1, '6': 1}
    # [[5,3],[3,1]]
    
               