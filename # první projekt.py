"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Josef Hubáček
email: jos.hubacek@gmail.com
discord: jose9990552
"""
# oddělovač
odd = "----------------------------------------"

# zadefinujeme si registrované uživatele
registrovani_uzivatele = {
    "bob" : "123",
    "ann" : "pass123",
    "mike" : "password123",
    "liz" : "pass123"
}

# texty
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

# uživatel zadá přihlašovací údaje
username = input("Vlož uživatelské jméno: ")
password = input("Vlož heslo: ")

# přihlášení
if username in registrovani_uzivatele and registrovani_uzivatele[username] == password:
    print(f"Welcome to the app {username}.")
    print("We have 3 texts to be analyzed.")
    print(odd)
    
    
else:
    print("$ python projekt1.py")
    print(f"username: {username}")
    print(f"password: {password}")
    print("unregistered user, terminating the program..")
    exit()
    

# výběr textu uživatelem
user_input = input("Enter a number between 1 and 3 to select: ")
print(odd)

# kontrola, zda je vstup číslo
if not user_input.isdigit():
    print("You did not enter a number from 1 to 3. Terminating the program.")
    exit()

# převod na integer
user_input = int(user_input) - 1 

if user_input >= 0 and user_input < len(TEXTS):
    selected_text = TEXTS[user_input]
    print(selected_text)
    print(odd)

else:
    print("You did not enter a number from 1 to 3. Terminating the program.")
    exit()


# Rozdělení textu na slova a smazaní interpunkce
selected_text = selected_text.replace(".", "")
selected_text = selected_text.replace(",", "")
words = selected_text.split()


# Inicializace proměnných pro statistiky
word_count = 0
title_case_count = 0
upper_case_count = 0
lower_case_count = 0
number_count = 0
number_sum = 0

# Projdeme každé slovo v textu
for word in words:
    # Spočítáme celkový počet slov
    word_count = word_count + 1
    
    # Vynechání 30N
    if word == "30N":
        continue
    
    # Spočítáme počet slov začínajících velkým písmenem
    if word.istitle():
        title_case_count = title_case_count + 1
    
    # Spočítáme počet slov psaných velkými písmeny
    if word.isupper():
        upper_case_count = upper_case_count + 1
    
    # Spočítáme počet slov psaných malými písmeny
    if word.islower():
        lower_case_count = lower_case_count + 1
    
    # Spočítáme počet čísel a součet všech čísel
    if word.isdigit():
        number_count = number_count + 1
        number_sum = number_sum + int(word)

# Výpis statistik
print(f"There are {word_count} words in the selected text.:")
print(f"There are {title_case_count} titlecase words.")
print(f"There are {upper_case_count} uppercase words.")
print(f"There are {lower_case_count} lowercase words.")
print(f"There are {number_count} numeric strings.")
print(f"The sum of all the numbers {number_sum}")
print(odd)


# Inicializace slovníku pro uložení četností délek slov
length_counts = {}

# Spočítání délek slov
for word in words:
    length = len(word)
    if length in length_counts:
        length_counts[length] = length_counts[length] + 1
    else:
        length_counts[length] = 1

# Vytisknutí grafu
print("LEN | OCCURENCES   | NR.")
print(odd)


counter = 1
for length in sorted(length_counts):
  stars = '*' * length_counts[length]
  print(f"{counter:3} | {stars:<12} | {length_counts[length]}")
  counter += 1

print(odd)









       