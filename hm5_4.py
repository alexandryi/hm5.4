def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, KeyError, IndexError) as e:
            return str(e)
    return inner

@input_error
def add_contact(contacts, name, phone):
    contacts[name]=phone
    print("Contact added.")

@input_error
def change_contact(contacts, name, new_phone):
    if name in contacts:
        contacts[name]=new_phone
        print("Contact updated.")
    else:
        print("Contact not found.")

@input_error
def show_phone(contacts, name):
    if name in contacts:
        print(contacts[name])
    else:
        print("Contact not found.")

@input_error
def show_all(contacts):
    for name, phone in contacts.items():
        print(f"{name}:{phone}")


def main():
    contacts={}
    print("How can I help you?")

    while True:
        user_input=input(">>> ")
        parts=user_input.strip().split(' ')
        command=parts[0].lower()

        if command=='exit' or command=='close':
            print("Good bye!")
            break
        elif command=='hello':
            print("How can I help you?")
        elif command=='add':
            if len(parts)!=3:
                print("Invalid command. Use format: add [name] [phone]")
            else:
                _, name, phone=parts
                add_contact(contacts, name, phone)
        elif command=='change':
            if len(parts)!= 3:
                print("Invalid command. Use format: change [name] [new_phone]")
            else:
                _, name, new_phone=parts
                change_contact(contacts, name, new_phone)
        elif command=='phone':
            if len(parts)!= 2:
                print("Invalid command. Use format: phone [name]")
            else:
                _, name=parts
                show_phone(contacts, name)
        elif command=='all':
            show_all(contacts)
        else:
            print("Unknown command. Type 'help' for available commands.")


if __name__ == "__main__":
    main()