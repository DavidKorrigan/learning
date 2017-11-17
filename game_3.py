#Create a list
gryffindor = ["Hermione Granger", "Ronald Weasley", "Harry Potter", "Lavender Brown"]

#Display the list of students
print ("\nList of the Gryffindor students:")
for a in gryffindor:
	print (a)

#Add a student to the list
gryffindor.append("Neville Longbottom")

#Display the list of students
print ("\nList of the Gryffindor students:")
for a in gryffindor:
	print (a)

#Sort the list alphabetically in ascending order
gryffindor.sort()

#Display the list of students
print ("\nList of the students sorted alphabetically:")
for a in gryffindor:
	print (a)

#Sort the list alphabetically in descending order
gryffindor.reverse()

#Display the list of students
print ("\nList of the students sorted alphabetically in descending order:")
for a in gryffindor:
	print (a)

#Display the list of students
gryffindor.remove("Lavender Brown")

#Display the list of students
print ("\nList of the students without Lavender Brown:")
for a in gryffindor:
	print (a)