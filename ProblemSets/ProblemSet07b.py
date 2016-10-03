# Problem Set 07b - Meet the Adopter

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