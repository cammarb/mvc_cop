from .model import Name
from .config import session
from .controller import *


def menu():
    print("""What would you like to do? \n
    1. See all names \n
    2. See a name \n
    3. Add a name \n
    4. Delete a name \n
    """)
    option = int(input("Enter option: "))
    if option == 1:
        show_all()
    elif option == 2:
        show_one(int(input("Enter id: ")))
    elif option == 3:
        add_one()
    elif option == 4:
        update_one(int(input("Enter id: ")))
    elif option == 5:
        delete()


def show_all():
    names = session.query(Name).all()
    for row in names:
        print("ID: ", row.id, "First Name: ",
              row.first_name, "Last Name: ", row.last_name)


def show_one(id):
    name = session.query(Name).get(id)
    print("ID: ", name.id, "First Name: ",
          name.first_name, "Last Name: ", name.last_name)


def add_one():
    first_name = input("Add first name: ")
    last_name = input("Add last name: ")
    add_name(first_name, last_name)


def update_one(id):
    first_name = input("Add first name: ")
    last_name = input("Add last name: ")
    update_name(first_name, last_name, id)


def delete():
    name_id = input("Enter id: ")
    delete_name(name_id)
