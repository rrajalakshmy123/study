from ast import main


def print_from_1_to_n(i,n) :
    if (i>n):
        return 
    else:
        print_from_1_to_n(i+1,n)
        print(i)
  

if __name__ == "__main__":

    print_from_1_to_n(0,5)
