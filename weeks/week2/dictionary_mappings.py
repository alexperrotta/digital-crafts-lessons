phonebook_dict = {
    'Alice': '703-493-1834',
    'Bob': '857-384-1234',
    'Elizabeth': '484-584-2923'
}

print phonebook_dict['Elizabeth']

# Add Kareem's number

phonebook_dict['Kareem'] = '938-489-1234'
print phonebook_dict['Kareem']

# Delete Alice's phone entry

del phonebook_dict['Alice']
# print phonebook_dict['Alice'] # will give you an error

print phonebook_dict # prints the whole dictionary so you can check to see if Alice is gone

# Change Bob's number to 968-345-2345

phonebook_dict['Bob'] = '968-345-2345'
print phonebook_dict['Bob']

# Print all phone entries

print phonebook_dict