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

# Returning a Simple value

# def get_foramtted_name(first_name, last_name):
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()

# musicaina = get_foramtted_name('jimi', "henry")
# print(musicaina)

def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name =f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('dolapo','tolu')
print(musician)

musician = get_formatted_name('dolapo', 'odesola', 'tolu')
print(musician)


# Returning a Dictionary

def build_person(first_name, last_name):
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('dolapo', 'odesola')
print(musician)


def build_person(first_name, last_name, age=None):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)

# Using function with while loop

# def get_foramtted_name(first_name, last_name):
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()

# while True:
#     print("\nPlease tell me your name:")
#     print("(enter 'q' at any time to quit)")

#     f_name = input("First name: ")
#     if f_name == 'q':
#         break
#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break

#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello, {formatted_name}")
    


#Ex 1.
def city_country(city, country):
    city_name = f"{city}, {country}"
    return city_name.title()

city_country_pair = city_country("santiago", "chile")
city_country_pair2 = city_country("abuja", "nigeria")
city_country_pair3 = city_country("paris", "france")

print(city_country_pair)
print(city_country_pair2)
print(city_country_pair3)

#Ex 2.
def make_album(artist_name, album_title, no_of_songs=None):
    album ={'name': artist_name, 'title': album_title}
    
    if no_of_songs:
        album['num'] = no_of_songs
    return album

album_make1 = make_album('juli', 'andrews', no_of_songs='2.4M')
album_make2 = make_album('don', 'moen', no_of_songs=4)
album_make3 = make_album('ron', 'kenoly', no_of_songs='6M')

print(album_make1)
print(album_make2)
print(album_make3)

#Ex 3

def make_album(artist_name, album_title, no_of_songs=None):
    album ={'name': artist_name, 'title': album_title}
    if no_of_songs:
        album['num'] = no_of_songs
    return album

while True:
    print("\nPlease enter your album details")

    print("(enter 'q' at any time to quit)")

    album_n = input("Album name: ")
    if album_n == 'q':
        break
    album_title = input("Title name: ")
    if album_title == 'q':
        break

    album_build = make_album(album_n, album_title)
    print(f"\nSo you like {album_build}")
    


