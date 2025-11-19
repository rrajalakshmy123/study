from ast import main

largestelementarray = [3, 5, 2, 9, 6]
def largestelement(array): 
    largestelement = array[0]
    for i in range(1, len(array)):
        if array[i]>largestelement:
            largestelement = array[i]
    print("The largest element is:", largestelement)
  
if __name__ == "__main__":

    largestelement(largestelementarray)
