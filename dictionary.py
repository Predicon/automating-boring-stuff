#The dictionary is the input and the expected output is list of items 
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def InventoryList(listofinventory):
#function is used for printing the ouput of each values in dictionary along with its key
	print('inventory')
	item_total=0

	for k,v in listofinventory.items():
		print(str(v)+" "+k)
		item_total+=v

	print('Total number of items' +  str(item_total))			

#instance of a class
InventoryList(stuff)

-----------------

"""Prints a  aligned table from a list of strings."""

table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]


def print_table(table):
    """Print a formatted, properly aligned table version of a list."""
    # Create list with zeroes equal to the length of input list
    col_widths = [0] * len(table)

    # Finds longest word in each sublists and sets col_width[x] to value
    count = 0
    while count < len(table):
        for item in table[count]:
            if len(item) > col_widths[count]:
                col_widths[count] = len(item)
        count += 1

    # Iterates over lists taking nth element from each
   

    for word in range(len(table[0])):
        for item in range(len(table)):
            print(table[item][word].rjust(col_widths[item]), end=' ')
        print()


print_table(table_data)