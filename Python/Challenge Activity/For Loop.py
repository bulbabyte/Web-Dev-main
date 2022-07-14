# Write an expression to print each price in stock_prices. Sample output for the given program:
"""
$ 34.62
$ 76.30
$ 85.05
"""
stock_prices = [34.62, 76.30, 85.05]
for price in stock_prices:
    print('$', price)

# Write a for loop to print each contact in contact_emails. Sample output for the given program:
"""
mike.filt@bmail.com is Mike Filt
s.reyn@email.com is Sue Reyn
narty042@nmail.com is Nate Arty
"""

contact_emails = {
    'Sue Reyn' : 's.reyn@email.com',
    'Mike Filt': 'mike.filt@bmail.com',
    'Nate Arty': 'narty042@nmail.com'
}

''' Your solution goes here '''
for contact in contact_emails:
    print(contact_emails[contact], 'is', contact)

