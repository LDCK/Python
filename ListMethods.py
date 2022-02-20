example_list = [1, 2, 3, 4]
#Using Append to add an additional item to the list
example_list.append(5)
print(example_list)

#Using Remove to remove the 5th item on the list
example_list.remove(5)
print(example_list)


#Another example of apending lists
garden = ["Tomatoes", "Grapes", "Cauliflower"]
#Append a new element
garden.append("Green Beans")
print(garden)


#Creating a new list and combining lists
orders = ["daisy", "buttercup", "snapdragon", "gardenia", "lily"]

# Create new orders here:
new_orders = ["lilac", "iris"]
orders_combined = orders + new_orders
print(orders_combined)

#New list using negative indices
shopping_list = ["eggs", "butter", "milk", "cucumbers", "juice", "cereal"]
#Selecting the last item on the list above
last_element = shopping_list[-1]
#Same as above
index5_element = shopping_list[5]
#printing both variables to verify
print(last_element)
print(index5_element)

#List using index and negative index
garden_waitlist = ["Jiho", "Adam", "Sonny", "Alisha"]
#Replacing Adam with Calla using the index method
garden_waitlist[1] = "Calla"
print(garden_waitlist)
#Replacing Alisha with Alex using a negative index
garden_waitlist[-1] = "Alex"
print(garden_waitlist)

#------ 2D Lists ------
#Creating 2D lists
Heights = [["Jenny", 61], ["Alexus", 70], ["Sam", 67], ["Grace", 64], ["Vik", 68]]
ages = [["Aaron", 15], ["Dhruti", 16]]

#Accessing 2D Lists
class_name_test = [["Jenny", 90], ["Alexus", 85.5], ["Sam", 83], ["Ellie", 101.5]]
print(class_name_test)

#Selecting and printing Sam's score from the list
#NOTE: The reason it's [2][1] is because Sam is the 3rd name of the 1st column.
#His score is the 2nd entry in that row.
class_name_test = [["Jenny", 90], ["Alexus", 85.5], ["Sam", 83], ["Ellie", 101.5]]
sams_score = class_name_test[2][1]
print(sams_score)

#Selecting and printing Ellie's score using Negative Indexing
class_name_test = [["Jenny", 90], ["Alexus", 85.5], ["Sam", 83], ["Ellie", 101.5]]
ellies_score = class_name_test[-1][-1]
print(ellies_score)

#Modifying 2D Lists
incoming_class = [["Kenny", "American", 9], ["Tanya", "Russian", 9], ["Madison", "Indian", 7]]
print(incoming_class)
#Using Positive indices
incoming_class[2][2] = 8
print(incoming_class)
#Using Negative indices
incoming_class[-3][-3] = "Ken"
print(incoming_class)