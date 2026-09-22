#UserName validator (problem 2)

username = input("Enter username: ")
if 5 <= len(username) <= 10 and username.isalnum():
    print("Valid username.")
else:
    print("Invalid username") 
