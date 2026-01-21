'''
Бот-асистент для ведення записної книжки з ім'ям та номером телефону

1) exit or close- to exit the application
2) add [ім'я] [номер телефону] - to add a new contact
3) change [ім'я] [новий номер телефону] - change contact
4) phone [ім'я] - to print number of contact 
5) all - to show all contacts

'''

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    if len(args) < 2:
        return "Помилка: введіть ім'я та номер телефону."
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    if len(args) < 2:
        return "Помилка: введіть ім'я та новий номер телефону."
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    return "Помилка: контакт не знайдено."   

def show_phone(args, contacts):
    if not args:
        return "Помилка: введіть ім'я."
    name = args[0]
    return contacts.get(name, "Помилка: контакт не знайдено.")

def show_all(contacts):
    if not contacts:
        return "Книга контактів порожня."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ").strip()
        if not user_input:
            continue
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
