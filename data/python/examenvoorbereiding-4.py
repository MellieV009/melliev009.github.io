names = ["Melvin", "Jay", "Rinus", "Koen", "Nico"]

# Sorteer de lijst van namen
names.sort()

# Print de gesorteerde lijst van namen
print("Gesorteerde lijst van namen:")
for name in names:
    print(name)

# Voeg een naam toe aan de lijst
new_name = input("Voer een naam in om toe te voegen aan de lijst: ")
names.append(new_name)

# Verwijder een naam uit de lijst
del_name = input("Voer een naam in om te verwijderen uit de lijst: ")
if del_name in names:
    names.remove(del_name)

# Sorteer de lijst van namen opnieuw
names.sort()

# Print de gewijzigde lijst van namen
print("Gewijzigde lijst van namen:")
for name in names:
    print(name)
    