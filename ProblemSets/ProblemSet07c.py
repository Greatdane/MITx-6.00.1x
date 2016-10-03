# Problem Set 07c - The Flexible and Fearful Adopters

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
# The Flexible Adopter
#
class FlexibleAdopter(Adopter):
    """
    A FlexibleAdopter still has one type of species that they desire,
    but they are also alright with considering other types of species.
    considered_species is a list containing the other species the adopter will consider
    Their score should be 1x their desired species + .3x all of their desired species
    """
    def __init__(self, name, desired_species, considered_species):
        '''
        Initializes FlexibleAdopter, a subclass of Adopter object class
        
        considered_species - a list of strings of alternative species that the person is interested in adopting.
        
        All of the inputs are the same as the Adopter
        '''
        self.name = name
        self.desired_species = desired_species
        self.considered_species = considered_species
    
    def get_score(self, adoption_center):
        '''
        Returns the score
        
        adopter_score - the value that the Adopter class's score method returns
        
        num_other - the number of animals the adoption center has of all the other considered species
        '''
        adopter_score = float(adoption_center.get_number_of_species(self.desired_species)) # Can we call directly from Adopter?
        
        num_other = 0
        for a in self.considered_species:
            num_other += float(adoption_center.get_number_of_species(a))        
        return adopter_score + ( 0.3 * num_other)
        

#
# The Fearful Adopter
#    
class FearfulAdopter(Adopter):
    """
    A FearfulAdopter is afraid of a particular species of animal.
    If the adoption center has one or more of those animals in it, they will
    be a bit more reluctant to go there due to the presence of the feared species.
    Their score should be 1x number of desired species - .3x the number of feared species
    """
    def __init__(self, name, desired_species, feared_species):
        '''
        Initializes FearfulAdopter, a subclass of Adopter object class
        
        feared_species - a string that is the name of the feared species.
        
        All of the inputs are the same as the Adopter
        '''
        self.name = name
        self.desired_species = desired_species
        self.feared_species = feared_species
    
    def get_score(self, adoption_center):
        '''
        Returns the score
        
        adopter_score - the value that the Adopter class's score method returns
        
        num_feared - the number of animals the adoption center has of the feared species
        '''      
        adopter_score = float(adoption_center.get_number_of_species(self.desired_species)) # Can we call directly from Adopter?
        
        num_feared = float(adoption_center.get_number_of_species(self.feared_species))       
        result =  adopter_score - (0.3 * num_feared)
        if result < 0:
            result = 0.0
        return result
        
# Testing..
Barry = FlexibleAdopter('Barry Jones', 'Dog', ['Cat', 'Hamster'])