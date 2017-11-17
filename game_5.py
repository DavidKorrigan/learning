#List of the ingredient used in the potion
ingredient = ["leech", "hair", "fly", "nail", "slime"]

#Open existing file with name of "recipe.txt" in writing
f = open("recipe.txt","w")

#Write the first & sedond line
f.write("Dear Severus Snape,\n")
f.write("Here under the list of ingredient I used for my potion of invincibility:\n")

#Write the list of ingredients
for a in ingredient:
	f.write("- " + a + "\n")
	
#Write the 2 last lines
f.write("Best regards,\nHarry Potter")

#Close the file
f.close()

#Open the file for append
f = open("recipe.txt","a")

#Add the line
f.write("\n14th November 2016")

#Close the file
f.close()