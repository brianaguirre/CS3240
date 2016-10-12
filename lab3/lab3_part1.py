__author__ = 'BrianAguirre'


#USER CREATION
user_name = ""
password = ""
data = {}

print("This program takes in usernames and password.")
print("If at any point you wish to quit, enter an empty string.")
user_name = input("Please enter the first user name:")
password = input("Enter a password for " + user_name + ":")

condition = True
if (user_name == ""):
    condition = False
elif (password == ""):
    condition = False
while(condition):
    data[user_name] = password
    user_name = input("Please enter another username:")
    password = input("Please enter another password for " + user_name + ":")

    if (user_name == ""):
        condition = False
    elif (password == ""):
        condition = False



#VERIFY USER LOGIN
print("")
print("Please login by enter a username and password.")
print("Enter an empty string to stop.")


check_user = input("Please enter the first user name:")
check_pass = input("Enter a password for " + check_user + ":")

condition2 = True
if (check_user == ""):
    condition2 = False
elif (check_pass == ""):
    condition2 = False
while(condition2):
    if (check_user in data):
        pass_on_file = data[check_user]
        if (check_pass == pass_on_file):
            print("Login success!")
        else:
            print("Login failed. Wrong Password.")

    else:
        print("Username not found.")

    check_user = input("Please enter another username:")
    check_pass = input("Please enter another password for " + check_user + ":")

    if (check_user == ""):
        condition2 = False
    elif (check_pass == ""):
        condition2 = False


if __name__ == "__main__":
    pass