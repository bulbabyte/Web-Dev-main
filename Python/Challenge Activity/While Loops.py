# Write an expression that executes the loop body as the user emters a mon-negative number 

user_num = 9

while user_num >= 0:
    print('Body')
    user_num = int(input( ))

print('Dont.')


# Write a while loop that prints user_num divided by 2 until user_num is less than 1. The value of user_num changes inside of the loop 

while user_num >= 1:
    user_num = user_num / 2
    print(user_num)

"""
if user_num was not set to = user_num / 2 -> it could have led to an infinte loop 
"""

# Write a while loop that prints the number doubled w.o exceedinf 100, follwd with a space

while num_insects <=100:
    print(num_insects, end=" ")
    num_insects = num_insects * 2 