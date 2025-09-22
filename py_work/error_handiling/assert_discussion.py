def is_palindrome (word):

    flag= True

    if word[::-1]:

        flag=False

    return flag

assert is_palindrome("madam")==True , "test case 1 failed "

assert is_palindrome("man")==False , "test case 2 failed" 


print(is_palindrome("complete"))


