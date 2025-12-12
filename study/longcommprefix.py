Input = ["flowers" , "flow" , "fly", "flight" ]
# Input =["dog" , "cat" , "animal", "monkey" ]

Output ="fl"

def longcommprefix(str):
    n=(len(str))
    first=str[0]
    for i in str[1:]:
       while not i.startswith(first):
           first = first[:-1] 
           print(first)
           if first == "":
                return ""
    return first


if __name__ == "__main__":
    out = longcommprefix(Input)
    print(out)