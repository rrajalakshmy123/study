s = "welcome to the jungle"
Output= "jungle the to welcome"
def reverse(s):
    output=s.split()
    output.reverse()
    out=' '.join(output)
    return out
    
if __name__ == "__main__":
    output=reverse(s)
    print(output)