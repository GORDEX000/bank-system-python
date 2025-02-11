import time

money = "1000"
genre = "male"
name = "Ezatullah"
lastname = "Nuurzaii"

def userinterface():
    print("Welcome back " + name + " to the bank" + "\n" + "money: " + money + "\n" + "genre: " + genre + "\n" + "name: " + name + "\n" + "lastname: " + lastname)

    while True:
        user = input()
        if user == '1':
            depositmoney()
            break
        else:
            print(f"something went wrong pls choose 1")


def depositmoney(money):
    user = input("How much do u want to deposit: ")
    money -= user

    print(f"u have {money} left \n\n\n")
    userinterface()



def login():
    username = "gordex"
    password = "12345678"
    attempts = 3

    while attempts > 0:
        userinput1 = input("enter username pls: ")
        userinput2 = input("enter password pls: ")
        if userinput1 == username and userinput2 == password:
            print("log in...")
            time.sleep(2)
            print("log in successful")
            userinterface()
            break
        else:
            attempts -= 1
            print(f"Incorrect username or password. {attempts} attempts remaining.")

    if attempts == 0:
        print("Too many failed attempts. Exiting...")
        time.sleep(1)
        exit()



def signin():
    print("Sign-in functionality is not implemented yet.")



while True:
    user = input("1. log in" + "\n" + "2. sign in")
    if user == '1':
        login()
        break
    elif user == '2':
        signin()
        break
    else:
        print("Wrong pls choose 1 for log in and 2 for sign in")