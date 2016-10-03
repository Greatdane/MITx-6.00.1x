# L11 Problem 6

class Queue(object):
    """ 
    A FIFO queue class. Insert an int, and when removing one, removes and returns
    the first one in. 
    """
    
    def __init__(self):
        """ Start with a blank list"""
        self.line = []
        
    def insert(self, e):
        """ Inserts one element into list"""
        self.line.append(e)
        
    def remove(self):
        """ Removes the earliest element from the list.
        Raises an error when the list becomes empty"""
        try:
            x =  self.line[0]
            self.line.remove(self.line[0])
            return x            
            # return self.line.pop(0) # Can also just use the pop method on lists!
        except:
            raise ValueError()
    