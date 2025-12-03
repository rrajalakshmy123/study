from ast import main 

def sumofn(n):
    if(n==0):
        return 0
    sum =sumofn(n-1)+n
    return sum

if __name__ == "__main__":
    sum=sumofn(5)
    print(sum)
