def input_error(func):
    """Декоратор для обработки ошибок ввода пользователя."""
    def wrapper(args, contacts):
        try:
            return func(args, contacts)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter the argument for the command"
    return wrapper


def parse_input(user_input: str):
    """Парсит команду и аргументы, приводит команду к нижнему регистру."""
    parts = user_input.strip().split()
    if not parts:
        return "", []
    cmd, *args = parts
    return cmd.lower(), args


@input_error
def add_contact(args, contacts: dict):
    """add <name> <phone> — добавляет новый контакт"""
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts: dict):
    """change <name> <new_phone> — меняет телефон существующего контакта"""
    name, phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return "Contact updated."


@input_error
def show_phone(args, contacts: dict):
    """phone <name> — показывает телефон по имени"""
    name = args[0]
    if name not in contacts:
        raise KeyError
    return contacts[name]


@input_error
def show_all(args, contacts: dict):
    """all — показывает все сохраненные контакты"""
    if not contacts:
        return "No contacts."
    return "\n".join(f"{n}: {p}" for n, p in contacts.items())


def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ("close", "exit"):
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
            print(show_all(args, contacts))
        elif command == "":
            print("Enter the argument for the command")
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
