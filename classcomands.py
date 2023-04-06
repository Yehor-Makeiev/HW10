from collections import  UserDict
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self) -> str:
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    pass



class Record:

    def __init__(self, name: Name, phone: Phone = None):
        self.name = name
        self.phones = [phone] if phone else [] 

    def add_phone(self, phone: Phone):
        self.phones.append(phone)

    def remove_phone(self, phone: Phone):
        self.phones.remove(phone)
   
    def change_phone(self, old_phone:Phone, new_phone:Phone):
        for i, p in enumerate(self.phones):
            if p.value == old_phone.value:
                self.phones[i] = new_phone
                return f'Pone {old_phone} change to {new_phone}'
        return f'Contact has no phone {old_phone}'


class AddressBook(UserDict):

    def add_record(self, record: Record):
        self.data[record.name.value] = record


