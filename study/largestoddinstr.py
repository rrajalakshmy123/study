inp = "0032579"
out="21463"

def largestodd(result):
    n = len(result)
    print(n)
    while(n>0):
        if result[n-1] in '13579': 
            last_odd_index = n
            break
        n=n-1

    if last_odd_index == -1:
        return ""
    result = result[:last_odd_index]
    result = result.lstrip("0")
    return result
    

if __name__ == "__main__":
    str=largestodd(inp)
    print (str)