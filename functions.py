# def greet_user(username):
#     """ Display a simple greeting ."""
#     print(f"Hello {username}, how you doing")

# greet_user("Tolu")


def favorite_book(title):
    print(f"One of my favorite books is {title}")

favorite_book("GOT")

# Postional Arguments

# def describe_pet(animal_type, pet_name):
#     print(f"\nI have a {animal_type}.")
#     print(f"\nMy {animal_type}'s name is {pet_name.title()}.")

# describe_pet('hamster', 'Hermione')

# Keyword Arguments

def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"\nMy {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='hamster', pet_name='Hermione')

# Default Values

def describe_pet(pet_name, animal_type="dog" ):
    print(f"\nI have a {animal_type}.")
    print(f"\nMy {animal_type}'s name is {pet_name.title()}.")

describe_pet('Willy')


# Make shirt

def make_shirt(message="I love python", size="large"):
    print(f"A shirt sized {size} is available. The message printed on it is {message.title()}")

make_shirt()    

make_shirt("medium")

make_shirt(size="small", message="coding is fun")

# Describe cities

def describe_city(city, country="Nigeria"):
    print(f"{city.title()} is in {country.title()}")
    print("")

describe_city("paris", "france")
describe_city("berlin", "germany")
describe_city("Abuja")
