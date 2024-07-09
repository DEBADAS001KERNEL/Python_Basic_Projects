class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        self.contacts[name] = phone
        print(f'Added contact: {name} - {phone}')

    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f'Removed contact: {name}')
        else:
            print(f'Contact "{name}" not found.')

    def search_contact(self, name):
        if name in self.contacts:
            print(f'Contact: {name} - {self.contacts[name]}')
        else:
            print(f'Contact "{name}" not found.')

    def view_contacts(self):
        if self.contacts:
            print('Your contacts:')
            for name, phone in self.contacts.items():
                print(f'{name}: {phone}')
        else:
            print('No contacts in the list.')

def main():
    contact_book = ContactBook()
    
    while True:
        print("\nOptions:")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. Search Contact")
        print("4. View Contacts")
        print("5. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter the name: ")
            phone = input("Enter the phone number: ")
            contact_book.add_contact(name, phone)
        elif choice == '2':
            name = input("Enter the name to remove: ")
            contact_book.remove_contact(name)
        elif choice == '3':
            name = input("Enter the name to search: ")
            contact_book.search_contact(name)
        elif choice == '4':
            contact_book.view_contacts()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
