from ast import main

largestelementarray = [-4,-8,-12,-15]
def slargestelement(array): 
    largestelement = float('-inf')
    slargestelement = float('-inf')
    for i in range(0, len(array)):
        if array[i]>largestelement:
            slargestelement = largestelement
            largestelement = array[i]
        elif array[i]<largestelement and array[i]>slargestelement:
            slargestelement=array[i]

    print("The second largest element is:", slargestelement)
  
if __name__ == "__main__":

    slargestelement(largestelementarray)
