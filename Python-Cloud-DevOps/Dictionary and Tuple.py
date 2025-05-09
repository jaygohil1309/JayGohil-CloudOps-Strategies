# Dictionary in Python :- Dictionary accepting all the data-types.

# Int, Float, Boolean, List etc.........
# Unindexable suppoter....

# dict = {
#     'key' : "value",
#     'name' : "apnacollege",
#     'learning' : "coding",
#     'age' : 22,
#     'is_adult' : True,
#     'marks' : 94.4
# }
# dict["name"] = "Jay Gohil" # This is Important in python_dict concept.....
# print(dict)

# print(dict)
# print(type(dict))

# Null_Dictionary :-

# null_dict = {}
# null_dict['name'] = "apnacollege"
# print(null_dict)

# Nested_Dictionary :-

# student = {
#     'name' : 'Jay',
#     'subjects' :{
#         'chem' : 97,
#         'phy' : 94,
#         'math' : 95
#     }
# }
# print(student) # print all data from nested_dict.....
# print(student['subjects']['chem']) # Print only all the subjects from dictionary.....

# print(student.keys()) # gives me all the keys from dictionary.....
# print(len(student))
# print(student.values()) # gives me all the values from dictionary.....

# print(student.items()) # returns all (key, value) pairs as tuples.....
# print(student['name2']) # Error
# print(student.get('name2')) # no error -> None.

# student.update({'city' : 'Kodinar'})
# print(student)
# student.update({'name' : 'Jay Gohil'}) # Updating the dictionary with old value to replace new value in this dict.
# print(student)

# Tuple in Python :-

# collection = {1,2,2,3,4, "hello", "world", "world", 4} # Ignore duplicate values.....
# print(collection)
# print(type(collection))
# print(len(collection))

# Empty_Set :-

# collection = {} # Empty_dict....
# collection = set() # Empty_set; Syntax
# print(type(collection))

# Set_Union() Method:-

# set1 = {1,2,3}
# set2 = {2,3,4}

# print(set1.union(set2)) # Output = {1,2,3,4,5}

# Set_Intersection() Method:-

set1 = {1,2,3}
set2 = (3,4,5)
print(set1.intersection(set2)) # Output = {3}

