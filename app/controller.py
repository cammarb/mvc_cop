from .model import Name
from .config import session


def add_name(firstname_input, lastname_input):
    new_name = Name()
    new_name.first_name = firstname_input
    new_name.last_name = lastname_input
    new_name.save()
    print("New name saved successfully.")


def update_name(firstname_input, lastname_input, id):
    name = session.query(Name).get(id)
    name.first_name = firstname_input
    name.last_name = lastname_input
    name.save()
    print("Name updated successfully.")


def delete_name(id):
    name = session.query(Name).get(id)
    name.delete()
    print("Name deleted successfully.")
