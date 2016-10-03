# L11 Problem 5

class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
    
    def __len__(self):
        """
        returns the len of self.vals, overwriting the len() build in python function
        """
        return len(self.vals)
            
    def intersect(self, e):
        """
        Assumes e is another intSet instance.
        
        Creates another intSet instance, newList. for every value in self.vals, 
        check to see if this value is a member of e for another intSet instance
        """
        newList = intSet()
        for x in self.vals:
            if e.member(x):
                newList.insert(x)
        return newList
        
        
#setA: {-15,-4,-3,1,5,10,11,17,19}
#setB: {-20,-10,-2,2,4,5,6,9,13,16}

setA = intSet()
setA.insert(-15)
setA.insert(-4)
setA.insert(-3)
setA.insert(1)
setA.insert(5)
setA.insert(10)
setA.insert(11)
setA.insert(17)
setA.insert(19)
setB = intSet()
setB.insert(-20)
setB.insert(-10)
setB.insert(-2)
setB.insert(2)
setB.insert(4)
setB.insert(5)
setB.insert(6)
setB.insert(9)
setB.insert(13)
setB.insert(16)

print setA.intersect(setB)
        