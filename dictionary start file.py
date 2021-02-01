phonebook = {
    "Chris": "555-1111",
    "Katie": "555-2222",
    "Joanne": "555-3333",
}

"""
print()
print("*****  start section 1 - print dictionary ********")
print()


print(phonebook)
print(len(phonebook))

mydictionary = dict(m=8, n=9)
print(mydictionary)

print()
print("*****  end section 1 ********")
print()


print()
print("*****  start section 2 - search dictionary ********")
print()


# phone = phonebook["Chris"] #way to access key of dictionary

# print(phone)

print(phonebook["Chris"])  # way to access key of dictionary

name = "Joe"
if name in phonebook:
    print(phonebook[name])
else:
    print("notfound")


print()
print("*****  end section 2 ********")
print()





print()
print("*****  start section 3 - edit/append dictionary ********")
print()


phonebook["Chris"] = "555-4444"  # updating value of key in a dictionary

phonebook[
    "Joe"
] = "555-0123"  # because key doesn't exit it is gonna add it to the dict and not give an error

print(phonebook)
print()
print("*****  end section 3 ********")
print()


print()
print("*****  start section 4 - delete/remove from dictionary ********")
print()

del phonebook["Chris"]
print(phonebook)
print()
print("*****  end section 4 ********")
print()


print()
print("*****  start section 5 - iterate through keys ********")
print()

for k in phonebook:
    print(k)  # printing the key
    print(phonebook[k])  ## rinting the value of the key

print()
print("*****  end section 5 ********")
print()


print()
print("*****  start section 6 - iterate through values  ********")
print()

for v in phonebook.values():  #.values can access the value directly in a dictionary
    print(v)

print()
print("*****  end section 6 ********")
print()


print()
print("*****  start section 7 - iterate through both key and value pair********")
print()

for (pair) in (phonebook.items()):  # changes the dictionaries key and value into tuple and retirves both key and value
    print(pair)

for (k,v,) in phonebook.items():  # better way of using items
    print(k, v)

print()
print("*****  end section 7 ********")
print()

print()
print("*****  start section 8 - using random and converting to list ********")
print()

"""
print()
print("*****  end section 8 ********")
print()

# clear method will wipe out the dictionary,
# get method will give you value but, it won't raise a key error. See example on slide
# pop
# pop item (currently not working)