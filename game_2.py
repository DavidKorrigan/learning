# Prices of the item to buy
robe = 4
hat = 3
gloves = 2
cloak = 3

# Prices of the candies
chocolate = 1.5
bean = 0.75

#Galleon you have in the wallet
wallet = 22

#Here the total you spent in the uniform
total_uniform = robe * 3 + hat + gloves + cloak

print ("Harry, you spent " + str(total_uniform) + " Galleon in your uniform.")

#Calculate the money remaining in the wallet
wallet = wallet - total_uniform

print ("Harry, you have " + str(wallet) + " Galleon to buy candies.")

if wallet >= chocolate + bean:
	print ("You can buy a chocolate bag and bag of beans.")
elif wallet >= chocolate:
	print ("You can buy a bag of chocolate or a bag of bean.")
elif wallet >= bean:
	print ("You can only buy a bag of bean.")
else:
	print ("You can not buy candies.")