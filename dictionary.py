# Step 1: Create the dictionary
emp = {
    'id': 101,
    'name': 'ranjit',
    'designation': 'Data Scientist',
    'salary': 85000
}

# Print the original dictionary
print("Original dictionary:")
print(emp)

# Step 2: Delete the 'designation' key
"""if 'designation' in emp:
    del emp['designation']"""

# Print the dictionary after deleting 'designation'
print("\nDictionary after deleting 'designation':")
print(emp)

# Step 3: Update the 'name' key
emp['name'] = 'rahul'

# Print the dictionary after updating 'name'
print("\nDictionary after updating 'name':")
print(emp)
