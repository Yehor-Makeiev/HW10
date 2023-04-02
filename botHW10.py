from collections import defaultdict, UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self) -> str:
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    pass


# Клас Record, який відповідає за логіку додавання/видалення/редагування необов'язкових полів та зберігання обов'язкового поля Name.
class Record:

    def __init__(self, name: Name, phone: Phone = None):
        self.name = name
        self.phones = []

    def add_phone(self, phone: Phone):
        self.phones.append(phone)

    def remove_phone(self, phone: Phone):
        self.phones.remove(phone)

    def change_phone(self, old_phone: Phone, new_phone: Phone):
        index = self.phones.index(old_phone)
        self.phones[index] = new_phone


class AddressBook(UserDict):

    def add_record(self, record: Record):
        self.data[record.name.value] = str(record)

    def change_record(self, record: Record):
        self.data.update({record.name.value: record})


phone_book = AddressBook()


def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            return "Give me name and phone please. For more information - enter 'Help' "
        except UnboundLocalError:
            return "You enter excessive words, please try again, or enter 'Help' "
        except KeyError:
            return "This name is not in the phone book, try again"

    return inner


def help(*args):
    return """1. To start - enter: 'Hello'

2. If you want add name and number - enter: 'add Name number' for example 'add Bill +380997654321'

3. If you want change number - enter: 'change Existing_Name new_nuber' for exemple 'change Bill +380997654321'

4. If you want see phone number for name - enter 'phone Existing_Name' for exemple 'phone Bill'

5. To show all phone book - enter 'show_all'

6. To stop working - enter 'exit', 'good bye', 'close' \n"""


def hello(*args):
    return "Hi, how can i help you?"


def exit(*args):
    return "Good bye! =*"


@input_error
def add(*args):
    list_of_param = args[0].split()
    name = Name(list_of_param[0])
    phone = Phone(list_of_param[1])
    rec = Record(name, phone)
    phone_book.add_record(rec)

    return f"I add {name} {phone} in phone_book!"


@input_error
def change(*args):
    list_of_param = args[0].split()
    name = Name(list_of_param[0])
    phone = Phone(list_of_param[1])
    rec = Record(name, phone)
    phone_book.change_record(rec)

    return f"I change number for {name} on {phone}"


@input_error
def phone(*args):
    list_of_param = args[0].split()
    name = str(list_of_param[0]).title()
    if name not in phone_book.keys():
        raise KeyError()

    return "".join(phone_book[name])


def show_all(*args):
    result = []
    for name, phones in phone_book.items():
        result.append(f"{name}: {''.join(phones)}")
    return "\n".join(result)


def no_command(*args):
    return "Unknown command, try again, or enter 'Help' "


COMMANDS = {help: "help",
            add: "add",
            change: "change",
            phone: "phone",
            hello: "hello",
            show_all: "show all"
            }


@input_error
def parser(text: str):
    tokens = text.split()
    if len(tokens) > 2:
        for i, token in enumerate(tokens):
            if token.lower() in COMMANDS.values():
                name = tokens[i + 1]
                phone = tokens[i + 2]
                result_str = f"{token.lower()} {name} {phone}"
    else:
        result_str = text.lower()
    return result_str


@input_error
def command_handler(text: str):
    for command, k_word in COMMANDS.items():
        if text.startswith(k_word):
            return command, text.replace(k_word, "").strip()
        if text.lower() in ["exit", "close", "good bye"]:
            return exit, None
    return no_command, None


def main():
    print(help())

    while True:
        user_input = input(">>>")
        pars = parser(user_input)
        command, data = command_handler(pars)
        print(command(data))
        print(phone_book)
        if command == exit:
            break


if __name__ == "__main__":
    main()
