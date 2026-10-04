print('===== PASSWORD MANAGER =====')
print('1. Add Password')
print('2. View Passwords')
print('3. Search Password')
print('4. Decrypted password')
print('4. Update Password')
print('5. Delete Password')
print('6. Exit')

import json

try:
    with open("password.json", "r") as file:
        listed = json.load(file)

except FileNotFoundError:
    listed = []

data=[]
def add_password():
    websiteName =input("Enter website name :").lower()
    userName=input("Enter Username :").lower()
    password=input("Enter password :")

    encrypted =''
    key=3
    for character in password:
        new_character =chr(ord(character) + key)
        encrypted += new_character
    print(f"Encrypted password :{encrypted}")

    data={
        'website':websiteName,
        'username':userName,
        'EncryptedPassword':encrypted,
    }
    listed.append(data)
    with open('password.json','w') as file:
        json.dump(listed ,file ,indent=4)
    print("Password add succesfull")
    print('=' * 30)

def view_password():
    try:
        with open('password.json','r') as file:
            print(json.load(file))
            print('=' * 30)
    except FileNotFoundError:
        print(listed)

def search_password():
    print("Enter Search by website name")
    webName=input("Enter website name to search :")
    for acount in listed:
        if webName == acount["website"]:
            print("Found")
            print(acount)
            print('=' * 30)
            break
    else:
        print("Website name not found")
   #not done
def decrypted_password():
    encrypPassword=input("Enter encrypted password :")
    for acount in listed:
        if encrypPassword == acount['EncryptedPassword']:
            print("Found")
            key=3
            decrypted=''
            for character in encrypPassword:
                new_character =chr(ord(character) - key)
                decrypted += new_character
            print(f"Decrypted password :{decrypted}")
            print('=' * 30)
            break
    else:
        print("Encrypted password not found")
def Update_password():
    ask=input("Enter website name to update :")
    for acount in listed:
        if ask == acount["website"]:
            print("Found")
            websiteName =input("Enter website name to update :").lower()
            userName=input("Enter Username to update :").lower()
            password=input("Enter password to update :")
            encrypted =''
            key=3
            for character in password:
                new_character =chr(ord(character) + key)
                encrypted += new_character
            print(f"Encrypted password :{encrypted}")

            acount["website"] = websiteName
            acount["username"] = userName
            acount["EncryptedPassword"] = encrypted

            data={
                'website':websiteName,
                'username':userName,
               'EncryptedPassword':encrypted,
            }
            listed.append(data)
            with open('password.json','w') as file:
                json.dump(listed ,file ,indent=4)
            print("Password update succesfull")
            print('=' * 30)
            break
    else:
        print("Website not found")
def delete_password():
    ask=input("Enter website name to Delete :")
    for acount in listed:
        if ask == acount['website']:
            print('Found')
            listed.remove(acount)
            print("Password Delete Succesfull")
            with open('password.json','w') as file:
                json.dump(listed,file,indent=4)
            print('=' * 30)
            break
    else:
        print("Website not found")

while True:
    option=input("Enter Option  (Add ,View ,Search ,Decrypted ,Update ,Delete ,Exit) :").lower().strip()
    if option == 'add':
        add_password()
    elif option == 'view':
        view_password()
    elif option == 'search':
        search_password()
    elif option == 'decrypted':
        decrypted_password()
    elif option == 'update':
        Update_password()
    elif option == 'delete':
        delete_password()
    elif option == 'exit':
        break
    else:
        print("Invaild option try again")