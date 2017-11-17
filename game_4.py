#Put your ingredients on the shelf
shelf = {'leech': 5, 'hair': 20, 'horn': 1, 'fly': 10, 'slime': 10}

#Display the list of ingredients
print ("Shelf after shopping:")
for ingredient in shelf:
    print (ingredient, shelf[ingredient])

#Add nails on the shelf
shelf['nail'] = 6

#Display shelf with nails
print ("\nShelf with nails:")
for ingredient in shelf:
    print (ingredient, shelf[ingredient])

#Remove what you used for the potion from the shelf
shelf['leech'] = shelf['leech'] - 3
shelf['hair'] = shelf['hair'] - 10
shelf['fly'] = shelf['fly'] - 2
shelf['nail'] = shelf['nail'] - 3
shelf['slime'] = shelf['slime'] - 5

#Display shelf after the potion
print ("\nShelf after the potion:")	
for ingredient in shelf:
    print (ingredient, shelf[ingredient])