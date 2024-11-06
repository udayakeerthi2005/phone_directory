import streamlit as st

class Node:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
        self.prev = None
        self.next = None

class PhoneDirectory:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def create_contact(self, name, phone_number):
        if not name or not phone_number:
            st.warning("Please enter both name and phone number")
            return
            
        new_node = Node(name, phone_number)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def delete_contact(self, name):
        if not name:
            st.warning("Please enter a name to delete")
            return
            
        current = self.head
        while current:
            if current.name == name:
                if current == self.head:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                elif current == self.tail:
                    self.tail = current.prev
                    self.tail.next = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                self.size -= 1
                st.success(f"Contact '{name}' deleted successfully!")
                return
            current = current.next
        st.warning(f"Contact '{name}' not found.")

    def search_contact(self, name):
        if not name:
            st.warning("Please enter a name to search")
            return
            
        current = self.head
        while current:
            if current.name == name:
                st.success(f"Name: {current.name}, Phone Number: {current.phone_number}")
                return
            current = current.next
        st.warning(f"Contact '{name}' not found.")

    def display_contacts(self):
        if self.is_empty():
            st.warning("Phone directory is empty.")
            return
            
        contacts = []
        current = self.head
        while current:
            contacts.append([current.name, current.phone_number])
            current = current.next
            
        st.write("### Contact List")
        st.table({"Name": [c[0] for c in contacts], 
                 "Phone Number": [c[1] for c in contacts]})

def main():
    st.title("Phone Directory App")
    
    if 'phone_directory' not in st.session_state:
        st.session_state.phone_directory = PhoneDirectory()

    name = st.text_input("Enter name:")
    phone_number = st.text_input("Enter phone number:")

    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("Add Contact"):
            st.session_state.phone_directory.create_contact(name, phone_number)
            if name and phone_number:
                st.success("Contact added successfully!")

    with col2:
        if st.button("Delete Contact"):
            st.session_state.phone_directory.delete_contact(name)

    with col3:
        if st.button("Search Contact"):
            st.session_state.phone_directory.search_contact(name)

    with col4:
        if st.button("Display Contacts"):
            st.session_state.phone_directory.display_contacts()

if __name__ == "__main__":
    main()