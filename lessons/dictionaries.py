"""Demonstrations of dictionary capabilities."""


# Declaring the type of dictionary 
schools: dict[str, int]

# Initialize to an empty dictionary 
schools = dict()

# set a key-value pairing in the dictionary 
schools["UNC"] = 19_400
schools["Duke"] = 6_717
schools["NCSU"] = 26_150

# Print a dictionary literal representation
print(schools)
print("HI")
print(len(schools))

# Access a value by its key -- ""lookup""
print(f"UNC has {schools['UNC']} students")

# Remove a key-value pair from a dictionary 
# by its key.
schools.pop("Duke")

# Test for existence of a key 
is_duke_present: bool = "Duke" in schools
print(f"Duke is present: {is_duke_present}")
# Another way this can be written:
# if "Duke" in schools:
#   print("Found the key 'Duke' in schools")
# else:
#   print("No key 'Duke' in schools")

# Update / Reassign a key-value pair
schools["UNC"] = 20_000
schools["NCSU"] = schools["NCSU"] + 200
# can also be written with relative assignment 
# schools["NCSU"] += 200

print(schools)

# Demonstration of dictionary literals 

# Empty dictionary literal 
schools = {} 
# Same as dict()
print(schools)

# Alternatively, initialize key-value pairs 
schools = {"UNC": 19400, "Dukie": 6717, "NCSU": 26150}  # one way of initializing it 
# can also use white space or new line characters to make it easier to read 
# same as saying 
# schools = {
#   "UNC": 19400, 
#   "Dukie": 6717, 
#   "NCSU": 26150}
print(schools)

# What happens when a key does not exist?
# print(schools["UNCC"])

# Example looping over the keys of a dict 
print("For in loop")
for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")
    print(type(school))
    print(type(schools[school]))