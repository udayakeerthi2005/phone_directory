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
        else:
            current = self.head
            st.table(data=[[c.name, c.phone_number] for c in [current] + [n for n in current.next]])

def main():
    st.title("Phone Directory App")

    phone_directory = PhoneDirectory()

    name = st.text_input("Enter name:")
    phone_number = st.text_input("Enter phone number:")

    if st.button("Add Contact"):
        phone_directory.create_contact(name, phone_number)
        st.success("Contact added successfully!")

    if st.button("Delete Contact"):
        phone_directory.delete_contact(name)

    if st.button("Search Contact"):
        phone_directory.search_contact(name)

    if st.button("Display Contacts"):
        phone_directory.display_contacts()

if __name__ == "__main__":
    main()