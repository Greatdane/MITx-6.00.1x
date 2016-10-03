# Problem Set 07d - AllergicAdopter and MedicatedAllergicAdopter

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
# The Allergic Adopter
#
class AllergicAdopter(Adopter):
    """
    An AllergicAdopter is extremely allergic to a one or more species and cannot
    even be around it a little bit! If the adoption center contains one or more of
    these animals, they will not go there.
    Score should be 0 if the center contains any of the animals, or 1x number of desired animals if not
    """
    def __init__(self, name, desired_species, allergic_species):
        '''
        Initializes AllergicAdopter, a subclass of Adopter object class.
        
        allergic_species -  a list of strings of one or more species that the adopter is allergic to.
        
        All of the inputs are the same as the Adopter
        '''
        self.name = name
        self.desired_species = desired_species
        self.allergic_species = allergic_species

    def get_score(self, adoption_center):
        '''
        Returns the score.
        
        Returns a value that is 0 if the adoption center has one or more of a species that the adopter is allergic to
        '''  
        for n in self.allergic_species:
            if adoption_center.get_number_of_species(n) > 0 :
                return 0.0
        return 1 * float(adoption_center.get_number_of_species(self.desired_species)) # Same code as Superclass Adopter 

#                
# The Medicated Allergic Adopter
#
class MedicatedAllergicAdopter(AllergicAdopter):
    """
    A MedicatedAllergicAdopter is extremely allergic to a particular species
    However! They have a medicine of varying effectiveness, which will be given in a dictionary
    To calculate the score for a specific adoption center, we want to find what is the most allergy-inducing species that the adoption center has for the particular MedicatedAllergicAdopter. 
    To do this, first examine what species the AdoptionCenter has that the MedicatedAllergicAdopter is allergic to, then compare them to the medicine_effectiveness dictionary. 
    Take the lowest medicine_effectiveness found for these species, and multiply that value by the Adopter's calculate score method.
    """
    def __init__(self, name, desired_species, allergic_species, medicine_effectiveness):
        '''
        Initializes MedicatedAllergicAdopter, a subclass of AllergicAdopter object class.
        
        medicine_effectiveness -  a dictionary of the effectiveness of the medicine for each animal. 
        
        All of the inputs are the same as the AllergicAdopter
        '''
        self.name = name
        self.desired_species = desired_species
        self.allergic_species = allergic_species
        self.medicine_effectiveness = medicine_effectiveness
    
    def get_score(self, adoption_center):
        '''
        Returns the score.        
        '''
        lowest = 1
        for n in self.allergic_species:
            if adoption_center.get_number_of_species(n) > 0 :
                if self.medicine_effectiveness[n] < lowest:
                    lowest = self.medicine_effectiveness[n]                
        return lowest * float(adoption_center.get_number_of_species(self.desired_species))
            
        
        