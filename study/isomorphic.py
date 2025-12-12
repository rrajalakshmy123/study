s = "ab"  
t = "cc"
Out= "true"

# s = "apple" , t = "bbnbm"

# Out= "false"

def isomorphic():
    mapping ={}
    mapped_values = set() 
    if(len(s)!=len(t)):
        return False
    for ch1, ch2 in zip(s, t):
        if ch1 in mapping and ch2!=mapping[ch1]:
            return False
        else:
            if ch2 in mapped_values:
                return False
        mapping[ch1] = ch2 
        mapped_values.add(ch2)
        print(mapped_values)
    return True
if __name__ == "__main__":
    x=isomorphic()
    print(x)

