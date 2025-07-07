import os
import json
import re

class ContactBook:
    def __init__(self,filename="01_projects/02_Contact_book_Project/contacts.json"):
        self.filename = filename
        self.contact_list = []
        self.load_contacts()
    
    @staticmethod
    def valid_phone_num(phone_num):
        if not phone_num.isdigit():
            print("Error: Please enter a valid phone number (only digits.)")
            return None
        
        if len(phone_num) != 10:
            print("Error: Phone number must contain 10 digits.")
            return None
        
        return int(phone_num)

    @staticmethod
    def name_validator(name):
        if len(name) < 3:
            print("❌ Name is too short. Minimum 3 characters required.")
            return None
        
        return name

    @staticmethod
    def email_validator(email_id):
        email_pattern = re.compile(r"^\w+@\w+\.\w+$")

        if not bool(email_pattern.match(email_id)):
            print('Error: Please enter valid email ID.')
            return
        
        return email_id

    def load_contacts(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename,'r') as file:
                    self.contact_list = json.load(file)
            
            except json.JSONDecodeError:
                print("Fresh contact list has been created for the user.")
        
        else:
            self.contact_list = []
    
    def save_contacts(self):
        try:
            with open(self.filename,'w') as file:
                json.dump(self.contact_list,file,indent=4)
        
        except Exception as e:
            print(f"Error while saving contacts: {e}")
    
    def add_contact(self):
        phone_num = input("\nEnter the phone number: ")
        phone_num = ContactBook.valid_phone_num(phone_num)

        if phone_num is None: 
            return

        for contact in self.contact_list:
            if phone_num == contact['phone']:
                print("\nThis contact already exists in your contact book.")
                print("\nHere is the details:")
                print(f"  👤 Name : {contact['name']}")
                print(f"  📞 Phone: {contact['phone']}")
                print(f"  📧 Email: {contact['email']}")
                return
        
        name = input("Enter the name of the person: ").title()
        name = ContactBook.name_validator(name)

        if name is None:
            return

        email_id = input("Enter the email id of the person: ")
        email_id = ContactBook.email_validator(email_id)

        if email_id is None:
            return
    
        self.contact_list.append({'name':name,'phone':phone_num,'email':email_id})
        try:
            self.save_contacts()
            print("\nContact details added Successfully!✅")
        
        except Exception as e:
            print(e)

    def view_contacts(self):
        if not self.contact_list:
            print("\n📭 No contacts found in your contact book. ❌")

        else:
            print("\n📒 Your Contact List:")
            for idx, contact in enumerate(self.contact_list, start=1):
                print(f"\nContact {idx}")
                print(f"  👤 Name : {contact['name']}")
                print(f"  📞 Phone: {contact['phone']}")
                print(f"  📧 Email: {contact['email']}")

    def search_contact(self):
        if not self.contact_list:
            print("No contact details available to search. ❌")

        else:
            print("\nEnter 1 to search by name 👤")
            print("Enter 2 to search by contact number 📞")
            print("Enter 3 to search by email id 📧")
            
            try:
                user_choice = int(input("Enter your choice: "))
            
            except ValueError:
                print("Error: Please enter valid number between 1 and 3.")
            
            else:
                match user_choice:
                    case 1:
                        contact_name = input("\nEnter the name 👤: ").title()
                        contact_name = ContactBook.name_validator(contact_name)

                        if contact_name is None:
                            return
                        
                        for contact in self.contact_list:
                            if contact_name == contact['name']:
                                print("\nContact with provided name: ")
                                print(f"  👤 Name : {contact['name']}")
                                print(f"  📞 Phone: {contact['phone']}")
                                print(f"  📧 Email: {contact['email']}")
                                break

                        else:
                            print("No contact found with provided name. ❌")

                    case 2:
                        phone_num = input("Enter the number to search 📞: ")
                        phone_num = ContactBook.valid_phone_num(phone_num)

                        if phone_num is None:
                            return
                        
                        for contact in self.contact_list:
                            if phone_num == contact['phone']:
                                print("\nContact with provided number: ")
                                print(f"  👤 Name : {contact['name']}")
                                print(f"  📞 Phone: {contact['phone']}")
                                print(f"  📧 Email: {contact['email']}")
                                break

                        else:
                            print("No contact found with provided contact number.❌")
                    
                    case 3:
                        email_id = input("Enter the email id: ")
                        email_id = ContactBook.email_validator(email_id)

                        if email_id is None:
                            return
                        
                        for contact in self.contact_list:
                            if email_id == contact['email']:
                                print("\nContact with provided email: ")
                                print(f"  👤 Name : {contact['name']}")
                                print(f"  📞 Phone: {contact['phone']}")
                                print(f"  📧 Email: {contact['email']}")
                                break
                        
                        else:
                            print("No contact found with provided email.❌")
                    case _:
                        print("Please enter number between 1 to 3")

    def del_contact(self):
        if not self.contact_list:
            print("No contact details available to delete ❌")
        
        else:
            phone_num = input("\nEnter the number to delete🗑️ : ")
            phone_num = ContactBook.valid_phone_num(phone_num)

            if phone_num is None:
                return

            for idx,contact in enumerate(self.contact_list):
                if phone_num == contact['phone']:
                    print("\nBelow contact from contact book is getting deleted...")
                    print(f"  👤 Name : {contact['name']}")
                    print(f"  📞 Phone: {contact['phone']}")
                    print(f"  📧 Email: {contact['email']}")

                    confirm = input("Do you really want to delete the contact number (y/n):").strip().lower()

                    if confirm == 'y':
                        self.contact_list.pop(idx)
                        self.save_contacts()
                        print("\nContact deleted successfully.✅")
                        return
                    
                    elif confirm == 'n':
                        print("Contact do not changed, deletion cancelled! ❌")
                        return

                    else:
                        print("Please enter valid choice, deletion has been cancelled.")
                        break

            print("Contact number not found!❌")

    def update_contact(self):
        if not self.contact_list:
            print("No contact details available to update or edit. ❌ ")
        
        else:
            phone_num = input("Enter contact number 📞 to update which contact: 📋")
            phone_num = ContactBook.valid_phone_num(phone_num)

            if phone_num is None:
                return

            for contact in self.contact_list:
                if phone_num == contact['phone']:
                    print("\n1: 👤 Update name")
                    print("2: 📞 Update contact number")
                    print("3: 📧 Update email id")

                    try:
                        user_choice = int(input("Enter your choice:"))
                    
                    except ValueError:
                        print("Error: Please enter valid number between 1 and 3.")
                    
                    else:
                        match user_choice:
                            case 1:
                                name = input("Enter the updated name 👤 : ").title()
                                name = ContactBook.name_validator(name)

                                if name is None:
                                    return
                                
                                contact['name'] = name
                                self.save_contacts()
                                break
                            case 2:
                                phone_num = int(input("Enter the updated number 📞 : "))
                                phone_num = ContactBook.valid_phone_num(phone_num)

                                if phone_num is None:
                                    return
                                
                                contact['phone'] = phone_num
                                self.save_contacts()
                                break
                            case 3:
                                email_id = input("Enter updated email id 📧 :")
                                email_id = ContactBook.email_validator(email_id)

                                if email_id is None:
                                    return
                                
                                contact['email'] = email_id
                                self.save_contacts()
                                break

                            case _:
                                print("Please choose between 1 to 3 only.")

            else:
                print("Please enter valid contact number 📞 to update ✏️ ")

if __name__ == "__main__":

    contacts = ContactBook()

    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact➕")
        print("2. View All Contacts👁️")
        print("3. Search Contact🔍")
        print("4. Delete Contact🗑️ ")
        print("5. Update Contact✏️ ")
        print("6. Quit🚪")

        try:
            user_choice = int(input("\nEnter your choice: "))
        
        except ValueError:
            print("Please enter a number between 1 and 6")
        else:
            match user_choice:
                case 1:
                    contacts.add_contact()

                case 2:
                    contacts.view_contacts()

                case 3:
                    contacts.search_contact()

                case 4:
                    contacts.del_contact()

                case 5:
                    contacts.update_contact()

                case 6:
                    print("\nHere is your complete contact list before exiting.")
                    contacts.view_contacts()
                    print("\nExiting...GOOD BYE!🚪👋")
                    break

                case _:
                    print("Please enter valid number between 1 to 6 ❌")