class Balloon(object):  # global python object
    def __init__(self, color, size, shape):
        self.color = color
        self.size = size
        self.shape = shape
        self.inflated = False
        self.working = True

    def inflate(self):
        if self.working:
            self.inflated = True
        else:
            print "You exploded this balloon. Idiot."

    def explode(self):
        self.inflated = False
        self.working = False
        print "BANG!"

    def deflate(self):
        self.inflated = False

class BigBalloon(Balloon): # this is a new class that takes some of the properties from the original class
    def __init__(self, color, shape):
        super(Balloon, self).__init__(color, 'Big', shape)  # refers to the original class
        

big_balloon = Balloon("red", "big", "round")
ballon2 = Balloon("blue", "small", "square")
