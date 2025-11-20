from ast import main

largestelementarray = [3, 5, 2, 9, 6]
def slargestelement(array): 
    largestelement = array[0]
    slargestelement = -1
    for i in range(1, len(array)):
        if array[i]>largestelement:
            slargestelement = largestelement
            largestelement = array[i]
        elif array[i]<largestelement and array[i]>slargestelement:
            slargestelement=array[i]

    print("The second largest element is:", slargestelement)
  
if __name__ == "__main__":

    slargestelement(largestelementarray)
