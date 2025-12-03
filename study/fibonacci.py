def fibonacii(n):
    if(n==0 or n==1):
        return n
    x=fibonacii(n-1)+fibonacii(n-2)
    return x
    
if __name__ == "__main__":
    y=fibonacii(5)
    print(y)
    