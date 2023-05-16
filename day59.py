def isPalindrome(s):
    return s == s[::-1]
  
  
# Driver code

while True:
    menu = input("1.Check\n2.Exit\n > ")

    if menu == "1":

        word = input("Input your word > ")
        ans = isPalindrome(word)
        if ans:
            print("Yes")
        else:
            print("No")
    elif menu == "2":
        print("Thank you")
        break
    else:
        break