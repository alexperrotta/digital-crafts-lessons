class Person(object):
    def __init__(self, name, email, phone, friends, greeting_count):
        # Attributes
        # We take in the argument
        # Assign it using self.attribute_name
        self.name = name  # tells the class that name is related to this class
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0

    def greet(self, other_person):
        self.greeting_count += 1
        print 'Hello %s, I am %s!' % (other_person.name, self.name)
        print 'The friend greeting count is: %s' % greeting_count

    def print_contact_info(self):
        print self.name
        print self.email
        print self.phone

    def add_friend(self, new_friend):
        self.friends.append(new_friend)
        print 'My new friend is: %s' % (new_friend)

    # Gets the number of friends
    def num_friends(self):
        print len(self.friends)



sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948', 'jordan', 0) # What you need to define Person)
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456', 'sonny', 0)
sonny.greet(jordan)
jordan.greet(sonny)

print "Sonny's Email: %s" % sonny.email
print "Sonny's Phone: %s" % sonny.phone
print "Jordan's Email: %s" % jordan.email
print "Jordan's Phone: %s" % jordan.phone

# sonny.print_contact_info()

# Add a new friend
# jordan.add_friend('Sonny')

# Call the number of friends
# jordan.num_friends()

# Count the number of greetings
sonny.greet(jordan)