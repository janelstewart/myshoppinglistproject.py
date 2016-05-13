my_shopping_lists_by_list_name = {}


def add_list(list_name):
	#check if list name exists in dictionary
	#if doesnt exist add list to dictionary
	if list_name not in my_shopping_lists_by_list_name:
		my_shopping_lists_by_list_name[list_name] = []
	

def add_item_to_list(list_name,item):
	#use list name to retrieve list 
	#check if item doesnt exists,
	list_name = list_name.lower()
	if list_name in my_shopping_lists_by_list_name:
		shopping_list = my_shopping_lists_by_list_name[list_name]
		if item in shopping_list:
			print "This %s is already in this list." % (item)
		else: 
			shopping_list.append(item)
			shopping_list.sort()
			print shopping_list
	else:
		print "This %s does not exist." % (list_name)
	#add item to list
	#if item does exists already then tell user its already there
	#print out current list after item added using list_sorter function

def remove_item_from_list(list_name,item):
	#check if item exists in list
	list_name = list_name.lower():
	if list_name in my_shopping_lists_by_list_name:
		shopping_list = my_shopping_lists_by_list_name[list_name]
		if item not in shopping_list:
			print "This %s does not exist." % (item)
		else:
			shopping_list.remove(item)
			shopping_list.sort()
			print shopping_list
	else:
		print "This %s does not exist." % (item)
	#if yes, remove item
	#if it doesnt exist tell user it doesnt exist
	#print out current list after removing item use list_sorter function

def remove_list(list_name):
	if list_name in my_shopping_lists_by_list_name:
		
	#check if list name is in dictionary
	#if yes, remove list
	#if not, tell user list does not exist 

#def list_sorter(list_name):
	#NOT NEEDED IF SORTING LIST THROUGHOUT FUNCTIONS
	#get list from dictionary 
	#sort list using .sort() and return sorted list 

def menu_option():
	#returns menu option 

def all_list():
	#need dictionary with key:value pairs
	#print 

def main():
	#ask for input 
	#use menu function to get choice then based on choice
	#you will decide which function to use 

if __name__ == '__main__':
	main()

