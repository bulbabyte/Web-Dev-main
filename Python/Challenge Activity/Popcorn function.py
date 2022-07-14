""" Define function print_popcorn_time() with parameter bag_ounces. If bag_ounces is less than 3, print "Too small". 
If greater than 10, print "Too large". Otherwise, compute and print 6 * bag_ounces followed by "seconds" """

def print_popcorn_time(bag_ounces):

    if bag_ounces < 3:
        print("too small")
    elif bag_ounces > 10:
        print("Too large")
    else:
        print((6 * bag_ounces), 'seconds')

print_popcorn_time(5)