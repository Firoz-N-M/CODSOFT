import random
import string

#PASSWORD GENRATION FUNCTION
def generate_password(length):
    password=''
    for i in range(length):
        password+=random.choice(string.ascii_letters+string.digits+string.punctuation)
    print('PASSWORD IS=',password)

print('WELCOME TO THE PASSWORD GENRATOR')

while True:
    #TAKING LENGTH OF PASSWORD FROM USER AND GENERATING PASSWORD
    l = int(input("\nEnter the desired password length: "))
    generate_password(l)
   
    
    # Option to continue or exit
    choice = input("Do you want to generate another password? (yes/no): ").lower()
    if choice == "no" or choice == "exit":
        print("Thank you for using the Password Generator!")
        break