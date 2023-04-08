from collections import  UserDict
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self) -> str:
        return str(self.value)


class Name(Field):
    def __str__(self) -> str:
        return str(self.value)


class Phone(Field):
    def __str__(self) -> str:
        return str(self.value)



class Record:

    def __init__(self, name: Name, phone: Phone = None):
        self.name = name
        self.phones = [phone] if phone else [] 

    def add_phone(self, phone: Phone):
        self.phones.append(phone)
        
    def change_phone(self, old_phone:Phone, new_phone:Phone):
        for i, p in enumerate(self.phones):
            if p.value == old_phone.value:
                self.phones[i] = new_phone
                return f'Phone {old_phone} change to {new_phone}'
        return f'Contact has no phone {old_phone}'
         
    def delete_phone(self, phone:Phone):
        for i, p in enumerate(self.phones):
            if p.value == phone.value:
                self.phones.pop(i)
                return f'Phone {phone} deleted'
    
    def __str__(self) -> str:
        phones = ", ".join([str(phone) for phone in self.phones])
        return f"{phones}"

class AddressBook(UserDict):

    def add_record(self, record: Record):
        self.data[record.name.value] = record


