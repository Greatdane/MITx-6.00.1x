# Problem Set 07e - The Sluggish Adopter

#
# Base class
#
class Adopter:
    """ 
    Adopters represent people interested in adopting a species.
    They have a desired species type that they want, and their score is
    simply the number of species that the shelter has of that species.

    """
    def __init__(self, name, desired_species):
        '''
        Initializes a Adopter object
            
        name - A string that represents the name of the adopter
    
        desired_species- A string that represents the desired species to adopt
        '''
        self.name = name
        self.desired_species = desired_species
    def get_name(self):
        '''
        Returns the name of the adopter
        '''
        return self.name 
    def get_desired_species(self):
        '''
        Returns the desired species of the adopter
        '''
        return self.desired_species
    def get_score(self, adoption_center):
        '''
        Returns the score
        The minimum value that a score can be is 0. 
        
        num_desired is a float of the number of the adopter's desired species that the adoption center has.
        '''
        num_desired = float(adoption_center.get_number_of_species(self.desired_species))
        return 1 * num_desired 

#                
# The Sluggish Adopter
#
class SluggishAdopter(Adopter):
    """
    A SluggishAdopter really dislikes travelleng. The further away the
    AdoptionCenter is linearly, the less likely they will want to visit it.
    Since we are not sure the specific mood the SluggishAdopter will be in on a
    given day, we will asign their score with a random modifier depending on
    distance as a guess.
    Score should be
    If distance < 1 return 1 x number of desired species
    elif distance < 3 return random between (.7, .9) times number of desired species
    elif distance < 5. return random between (.5, .7 times number of desired species
    else return random between (.1, .5) times number of desired species
    """
    def __init__(self, name, desired_species, location):
        '''
        Initializes SluggishAdopter, a subclass of Adopter object class.
        
        location - is a tuple of floats of the (x, y)
        
        All of the other inputs are the same as Adopter.
        '''
        Adopter.__init__(self, name, desired_species)
        self.location = (float(location[0]), float(location[1]))
        
    def get_linear_distance(self, to_location):
        '''
        Imports math modulet to calculate square root (math.sqrt)
        
        Returns the formula of the square root of (x1 - y1)^2 + (x2 - y2)^2 were x is 
        the input to_location and y is self.location.
        '''
        import math
        return math.sqrt(((to_location[0]-self.location[0])**2) + ((to_location[1]-self.location[1])**2))
        
    def get_score(self, adoption_center):
        '''
        Imports the random module to create a random number between two variables (random.uniform(x, y))
        
        Returns the score, based on distance, and a random variable between two set ammounts.
        '''
        import random
        # num_desired is taken from the original Adopter to get a score
        num_desired = float(adoption_center.get_number_of_species(self.desired_species))
        # To calculate the distance between Mr Slugglish and the adoption center
        distance = self.get_linear_distance(adoption_center.get_location()) 
        
        if distance < 1:
            return 1 * num_desired
        elif distance < 3:
            return random.uniform(0.7, 0.9) * num_desired
        elif distance < 5:
            return random.uniform(0.5, 0.7) * num_desired
        elif distance >= 5:
            return random.uniform(0.1, 0.5) * num_desired 
        