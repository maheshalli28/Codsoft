#Created on Sun Nov  5 15:19:11 
#Contact Information: Store name, phone number, email, and address for each contact.
#Add Contact: Allow users to add new contacts with their details.
#View Contact List: Display a list of all saved contacts with names and phone numbers.
#Search Contact: Implement a search function to find contacts by name or phone number.
#Update Contact: Enable users to update contact details.
#Delete Contact: Provide an option to delete a contact.
#User Interface: Design a user-friendly interface for easy interaction.


contact_list = []

# Function to add a new contact
def add_contact():
    contact_name = input("Enter store name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contact = {
        "Contact Name": contact_name,
        "Phone Number": phone_number,
        "Email": email,
        "Address": address
    }
    contact_list.append(contact)
    print("Contact added successfully!")

# Function to view the contact list
def view_contact_list():
    print("Contact List:")
    if contact_list:
         for i,contact in enumerate(contact_list):
             print(f"{i+1}. {contact['Contact Name']}     {contact['Phone Number']}    {contact['Email']}                 {contact['Address']} ")
    else:
          print("Your contact is empty")
   
# Function to search for a contact by name or phone number
def search_contact():
    search_query = input("Enter the name or phone number to search: ")
    found_contacts = []
    for contact in contact_list:
        if search_query in contact["Contact Name"] or search_query in contact["Phone Number"]:
            found_contacts.append(contact)
    if found_contacts:
        print("Search results:")
        for i, contact in enumerate(found_contacts):
            print(f"{i + 1}. {contact['Contact Name']}:  {contact['Phone Number']}")
    else:
        print("No matching contacts found.")

# Function to update contact details
def update_contact():
    contact_index = int(input("Enter the index of the contact you want to update: ")) - 1
    if 0 <= contact_index < len(contact_list):
        contact = contact_list[contact_index]
        print("Current Contact Information:")
        for key, value in contact.items():
            print(f"{key}: {value}")
        new_info = input("Enter the updated information (e.g,'Contact Name/Number: New Name/Number'):")
        key, new_value = new_info.split(": ")
        contact[key] = new_value
        print("Contact updated successfully!")
    else:
        print("Invalid contact index.")

# Function to delete a contact
def delete_contact():
    contact_index = int(input("Enter the index of the contact you want to delete: ")) - 1
    if 0 <= contact_index < len(contact_list):
        del contact_list[contact_index]
        print("Contact deleted successfully!")
    else:
        print("Invalid contact index.")

# User interface 
while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice (1/2/3/4/5/6): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contact_list()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Thank You")
        break
    else:
        print("Invalid choice. Please try again.")
