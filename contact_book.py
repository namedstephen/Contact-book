import json

def show_contacts(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    for name, phone in data["contacts"].items():
        print(f"{name} : {','.join(phone)}")    


def add_contact(filename, name, phone):
    with open(filename, 'r+') as f:
        data = json.load(f)
        data["contacts"][name] = phone
        f.seek(0)
        json.dump(data,f)
        f.truncate()

def update_contact(filename, name, phone):
    with open(filename, 'r+') as f:
        data = json.load(f)
        if name in data["contacts"]:
            data["contacts"][name] = phone
            f.seek(0)
            json.dump(data,f)
            f.truncate()
        else:
            print("Contact not found")

def delete_contact(filename, name):
    with open(filename, 'r+') as f:
        data = json.load(f)
        if name in data["contacts"]:
            del data["contacts"][name]
            f.seek(0)
            json.dump(data,f)
            f.truncate()
        else:
            print("Contact not found")

def add_phone_number(filename, name, phone):
    with open(filename, 'r+') as f:
        data = json.load(f)
        if name in data["contacts"]:
            data["contacts"][name].append(phone)
            f.seek(0)
            json.dump(data,f)
            f.truncate()
        else:
                print("Contact not found")

def delete_phone_number(filename, name, phone):
    with open(filename, 'r+') as f:
        data = json.load(f)
        if name in data["contacts"]:
            data["contacts"][name].remove(phone)
            f.seek(0)
            json.dump(data,f)
            f.truncate()
        else:
                print("Contact not found")

def main():
    filename = "contacts.json"
    while True:
        print("1. Show contacts")
        print("2. Add contact")
        print("3. Update contact")
        print("4. Delete contact")
        print("5. Add phone number")
        print("6. Delete phone number")
        print("7. Exit")
        choice = input("Your choice is:\t")
        if choice == "1":
            show_contacts(filename)

        elif choice == "2":
            name = input("Enter contact name:\t").lower()
            phone = input("Enter contact phone:\t").split(", ")
            add_contact(filename, name, phone)
            show_contacts(filename)

        elif choice == "3":
            name = input("Enter contact name:\t").lower()
            phone = input("Enter contact phone:\t").split(", ")
            update_contact(filename, name, phone)
            show_contacts(filename)
            
        elif choice == "4":
            name = input("Enter contact name:\t").lower() 
            delete_contact(filename, name)
            show_contacts(filename)

        elif choice == "5":
            name = input("Enter contact name:\t").lower()
            phone = input("Enter contact phone:\t")
            add_phone_number(filename, name, phone)
            show_contacts(filename)

        elif choice == "6":
            name = input("Enter contact name:\t").lower()
            phone = input("Enter contact phone:\t")
            delete_phone_number(filename, name, phone)  
            show_contacts(filename)

        elif choice == "7":
            break

        else:
            print("invalid opton\n")
            

main()
