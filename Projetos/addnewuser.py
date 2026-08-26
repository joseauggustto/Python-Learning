# o nome pode ter no maximo 10 caracteres
# a senha pode ter no maximo 10 caracteres

import os 

def new_user():

    confirm = input("Do you want to add a new user? (y/n): ")

    while confirm == "y":
        user_name = input("Enter the name user: ")
      #  password = input("Enter the password: ")

        if not user_name:
            print("User name is empty")
            continue

       # if not password:
          #  print("Password is empty")
          #  continue

       # if len(user_name) > 10 or len(password) > 10:
           # print("User and password is too long - max 10 characters")
           # continue

      #  if " " in user_name or " " in password:
           # print("User name and password should not contain spaces")
           # continue

        os.system("sudo adduser" + user_name)

        print("User created successfully!")
        confirm = input("Do you want to add another user? (y/n): ")

    print("Goodbye!")

new_user()

# Ainda falta terminar e completar com todas as funções necessárias!!!! 
