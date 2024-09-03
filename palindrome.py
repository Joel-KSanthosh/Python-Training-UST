word : str = input("Enter a word : ")
reverse : str = word[::-1]
if word == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")