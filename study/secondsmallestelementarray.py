from ast import main

smallestelementarray = [3, 5, 2, 9, 6]
def ssmallestelement(array): 
    smallesttelement = array[0]
    ssmallestelement = -1
    for i in range(1, len(array)):
        if array[i]<smallesttelement:
            ssmallestelement = smallesttelement
            smallesttelement = array[i]
        elif array[i]>smallesttelement and array[i]<ssmallestelement:
            ssmallestelement=array[i]

    print("The second largest element is:", ssmallestelement)
  
if __name__ == "__main__":

    ssmallestelement(smallestelementarray)