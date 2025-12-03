

def pow(a,k):
    if k==0:
        return 1
    else:
        return a*pow(a,k-1)
    
if __name__ == "__main__":
    result = pow(2,7)
    print(result)
