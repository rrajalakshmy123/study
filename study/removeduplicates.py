from ast import main

array =[1,2,5,5,5]

def removeduplicates(arrayforchecking):
    uniqueelement = set(array)
    return uniqueelement
if __name__ == "__main__":

    x=removeduplicates(array)
    u= list(x)
    print(u)