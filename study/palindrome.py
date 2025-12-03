def pallindrome(x, start, end):
    if start >= end:
        print("palindrome")
        return
    
    if x[start] != x[end]:
        print("not palindrome")
        return
    
    pallindrome(x, start + 1, end - 1)


if __name__ == "__main__":
    pallindrome('malayalan', 0, 8)

    