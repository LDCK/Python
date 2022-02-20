#Last semester gradebook
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

#Current semester gradebook
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]
print(gradebook)
#Add additional subjects
gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])
#Append the grade
gradebook.append(["visual arts", 98])
print(gradebook)
#Remove the pass mark
gradebook[2].remove(85)
print(gradebook)
#Append the mark as "Pass"
gradebook[2].append("Pass")
print(gradebook)
#Combine the 2 gradebooks
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)